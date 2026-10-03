# System design analysis

[Portfolio](../README.md) · English | [日本語](system-design.ja.md)

## 1. Architectural intent

I designed the system around two responsibilities: **hierarchical agents** coordinate the fleet, and **network agents** coordinate communication. GPS and onboard sensors support navigation, while satellite communication connects drones with the control system.

The tables distinguish the design in the patent from the engineering work needed to implement it. I also outline data structures, failure handling, and tests that I would use in a future implementation.

![Architecture](../assets/fig-01-system-architecture-en.svg)

## 2. Responsibility boundaries

| Boundary | Patent design | Implementation proposal |
|---|---|---|
| Platform → AI control | Receive orders and determine the customer location | Validate the destination and delivery-point eligibility before assignment; define when location updates may change a mission |
| Hierarchical agents → drone fleet | Select drones, schedule work, and optimize routes | Maintain one authoritative active assignment per drone and version route changes |
| Network agents ↔ participants | Exchange real-time information among drones, control center, and customers | Specify message ordering, duplicate handling, freshness, and recovery after disconnection |
| Drone sensors → navigation | Detect obstacles and adjust the flight path | Define onboard decision authority, sensor-health checks, and behavior when observations disagree |
| AI control → customer | Send a pre-arrival alert | Define ETA refresh, retry, deduplication, and delivery receipt for notifications |
| Operations → learning | Retain paths, images, and sensor readings for improvement | Validate datasets and candidate models before deploying an updated model |

## 3. Agent coordination

![Agent coordination sequence](../assets/fig-02-agent-coordination-en.svg)

The platform sends the request and destination to the hierarchical agents. Network agents relay the mission to the drone, carry position and status updates back, and deliver revised guidance. Before arrival, the customer receives an alert.

This sequence defines the responsibilities and exchanges. API design, storage ingestion, and ownership of the arrival-time calculation remain implementation decisions.

## 4. Proposed data structures

I would use the following records to connect orders, missions, telemetry, and delivery outcomes. These are proposed fields for implementation.

| Record | Example fields | Reason |
|---|---|---|
| Delivery request | `request_id`, `destination`, `delivery_point_id` | Correlate an order with an intended handoff location |
| Mission assignment | `mission_id`, `drone_id`, `route_version`, `issued_at` | Identify the active mission and reject an obsolete route |
| Telemetry | `mission_id`, `observed_at`, `position`, `battery_state`, `sensor_health` | Check data freshness and the drone's ability to continue |
| Arrival notification | `mission_id`, `eta`, `notification_id`, `sent_at` | Avoid duplicated alerts and evaluate timing |
| Delivery record | `mission_id`, `outcome`, `completed_at`, `data_references` | Link the operational outcome to retained evidence |

Time sources, coordinate reference systems, units, access control, and schema evolution would need to be specified before implementation.

## 5. Failure handling

![Safety responses and implementation conditions](../assets/fig-05-safety-responses-en.svg)

The safety design combines redundant communication, obstacle avoidance, continuous monitoring, and return or landing procedures. Each response needs operating limits and clear activation conditions.

| Scenario | Design basis | Implementation proposal | Test records |
|---|---|---|---|
| Communication interruption | Redundant links; return or safe landing | Use a bounded communication timeout and a defined local fallback policy | Simulated link-loss timeline, chosen response, recovery behavior |
| Obstacle detected | Sensors and automatic route adjustment | Define minimum detection and avoidance performance for the intended environment | Scenario coverage, intervention count, avoidance outcome |
| Power problem | Return-to-base or safe-landing description | Specify low-energy thresholds and controlled-landing feasibility; complete power loss needs separate handling | Energy budget and controlled fault-injection results |
| Changing weather | Dynamic routing from weather/environment data | Establish conditions for rerouting, holding, or terminating a mission | Decision trace against predefined operating limits |
| Stale or duplicated command | Continuous coordination | Version assignments and make repeated messages safe to process | Message replay and out-of-order tests |
| Delivery point unavailable | Predefined drop-off location | Define handoff confirmation and an abort or alternate-site procedure | Delivery-point rejection and recovery cases |

Handling stale commands and unavailable delivery points requires additional procedures beyond the patent description. The table sets out the tests needed to evaluate them.

## 6. Security and operational data

The design calls for encrypted and authenticated satellite communication, quantum-resistant cryptographic protocols, and encrypted storage of images, sensor readings, and flight paths.

**Work needed for implementation:**

- Identify authenticated endpoints, manage device keys, and define revocation and rotation.
- Select concrete cryptographic protocols and assess their computational and communication cost on the drone platform.
- Define how the system responds to unavailable or inconsistent positioning and communication inputs.
- Limit access to customer locations and camera data, and set retention and deletion rules.
- Record dataset and model versions so a change in navigation behavior can be traced to its inputs.

These requirements need a concrete protocol suite, a threat model, and tests for positioning integrity before deployment.

## 7. Learning lifecycle

![Operational learning cycle](../assets/fig-06-learning-flow-en.svg)

Flight data feeds back into navigation, energy management, and logistics planning. I would put validation and release checks between model training and deployment:

1. Associate flight records with mission outcomes and sensor-health context.
2. Validate timestamps, missing observations, labels, and data provenance.
3. Separate training and evaluation data by mission and operating scenario.
4. Evaluate a candidate model against route, energy, and safety criteria.
5. Release approved versions with a rollback path and monitor subsequent behavior.

This proposed release process would allow models to improve from delivery data while keeping updates reviewable and reversible.

## 8. Evaluation plan

I would start with scenario-based simulation, then move to controlled flight trials. The table defines the proposed measures; baselines, acceptance thresholds, and datasets still need to be established.

| Question | Proposed measure | Evaluation approach |
|---|---|---|
| Does the system complete accepted work? | Successful deliveries / accepted missions; report rejection and cancellation separately | Scenario-based simulation followed by controlled trials |
| Does coordination adapt to change? | Replanning time and valid reassignment rate | Inject weather, availability, and route changes |
| Is the arrival alert useful? | Distribution of actual arrival time minus alert time | Compare delivery events with notification logs; inspect deviation from the approximately five-minute target |
| What is the energy cost? | Watt-hours / successful delivery, stratified by payload and route | Measure comparable missions and disclose operating conditions |
| How does communication recover? | Outage duration, recovery time, and fallback outcome | Controlled interruption and recovery scenarios |
| Are safety responses consistent? | Correct response rate per predefined fault scenario | Review fault-injection traces against explicit acceptance criteria |
| Are cost and emissions goals supported? | Cost / completed delivery; energy and emissions accounting under stated assumptions | Compare like-for-like routes, payloads, and service conditions |

Cost and environmental benefits need comparison under equivalent routes, payloads, and service conditions. The measures above are an evaluation plan, with results to be established through testing.

## 9. Design contribution

My contribution was to define how fleet decisions, drone operation, customer communication, and learning fit together in one delivery system. I developed the invention and wrote the system specification, including agent responsibilities, operating procedures, and safety requirements.
