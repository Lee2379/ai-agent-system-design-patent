# AI Agent & System Design

**Autonomous Drone Delivery Patent**

**Language:** English | [日本語](japanese-readme.md)

**Granted patent · CIPC 2025/09550 · 28 January 2026**

![FIG. 1 — System architecture with numbered AI agents, communications, drone fleet, and data components](assets/fig-01-system-architecture-en.svg)

*Six technical drawing sheets, available in English and Japanese. [Drawing index and reference numerals](assets/README.md).*

**Visual walkthrough:** [Architecture](#multi-agent-system-architecture) · [Agent coordination](#how-the-agents-coordinate) · [Delivery lifecycle](#delivery-lifecycle) · [Safety and learning](#safety-security-and-learning)

## About this project

I designed a multi-agent AI system for autonomous drone delivery and wrote the patent specification. The patent was granted by **CIPC** on **28 January 2026**, with publication number **ZA202509550B**.

The design separates fleet scheduling and routing from communication between drones, the control center, and customers. It brings these responsibilities together with autonomous navigation, arrival notifications, and the reuse of flight data for AI improvement.

My work covered the system architecture, agent responsibilities, delivery workflow, communications requirements, and safety behavior. This repository documents that design, with a [technical analysis](docs/system-design.md), [claim map](docs/claim-map.md), and the [patent specification](source/specification.txt).

**Areas of focus:** Multi-agent AI · system design · autonomous systems · technical writing

## Granted patent

**Artificial Intelligence-Based Smart Drone Delivery System Using AI Multi-Agent Technology.**

| Patent information | Record |
|---|---|
| Patent office | CIPC |
| Patent number | 2025/09550 |
| Publication number | ZA202509550B |
| Filing / priority date | 11 November 2025 |
| Grant / registration date | 28 January 2026 |
| Publication date | 28 January 2026 |

## Invention at a glance

| Dimension | Design |
|---|---|
| Application | Autonomous parcel delivery |
| Geographic context | South Korea, Japan, and China |
| Coordination | Hierarchical fleet management and network-agent cooperation |
| Drone capabilities | GPS positioning, sensors, cameras, autonomous navigation, electric propulsion |
| Connectivity | Satellite communication with encrypted and authenticated exchanges |
| Customer experience | Order placement, location-aware assignment, arrival alert, designated delivery point |
| Data lifecycle | Flight paths, sensor readings, and images stored for subsequent AI improvement |
| Published material | Technical case study, architecture diagrams, source specification, and claim mapping |

This is a patent and system design project. The evaluation plan sets out how to test a future implementation; flight-test results and performance benchmarks are not included.

## Problem and design objectives

I approached delivery as a coordination problem: a fleet-wide plan has to adapt to the conditions each drone encounters. Dense cities, mountainous terrain, and dispersed destinations make that connection especially important.

| Design objective | Mechanism in the specification | Intended value |
|---|---|---|
| Coordinate fleet resources | Hierarchical agents schedule drones and determine routes | More consistent assignment and fleet management |
| Adapt to changing conditions | AI agents update paths using traffic, weather, and environmental data | Responsive navigation |
| Keep participants informed | Network agents exchange information among drones, the control center, and customers | Delivery visibility and coordinated operations |
| Make receipt predictable | Text or app notification approximately five minutes before arrival | Time for the customer to prepare for receipt |
| Extend delivery access | Autonomous electric drones and designated delivery points | Service options for difficult-to-reach locations |
| Improve future operations | Retain operational data for learning and optimization | Better-informed navigation and logistics planning |

The [evaluation plan](docs/system-design.md#8-evaluation-plan) describes how I would assess these objectives.

## Multi-agent system architecture

The architecture combines a central AI control server with two complementary agent responsibilities:

| Component | Responsibility | Main information handled |
|---|---|---|
| **Hierarchical AI agents** | Fleet control, drone assignment, scheduling, routing, and coordination | Delivery requests, drone availability, destinations, route decisions |
| **Network AI agents** | Communication, data exchange, and cooperation among drones, the control center, and customers | Status updates, coordination information, and customer messages |
| **Autonomous drones** | Execute navigation and delivery; detect obstacles and respond to local conditions | GPS coordinates, sensor readings, camera images, and flight status |
| **Customer platform** | Accept orders and deliver text/app alerts | Delivery requests, destination information, and arrival notifications |
| **Operational data store** | Retain delivery information in an encrypted cloud database for AI improvement | Flight paths, sensor readings, and images |

I separated the agents by responsibility: hierarchical agents make fleet decisions, while network agents handle information exchange. Process placement and communication protocols remain implementation decisions.

<details>
<summary><strong>FIG. 4 — Drone functional components</strong></summary>

![GPS, sensors, cameras, communication modules, and electric propulsion within the drone boundary](assets/fig-04-drone-components-en.svg)

Components 141–145 cover positioning, sensing, communication, and propulsion. The drawing shows their functions; detailed hardware design is a separate implementation step.

</details>

### How the agents coordinate

![Sequence of delivery requests, assignment, telemetry, guidance updates, and customer notifications](assets/fig-02-agent-coordination-en.svg)

Hierarchical agents determine assignments and routes. Network agents carry coordination information between participants. The drone reports its position and status so guidance can be updated during delivery. This sequence illustrates responsibilities and information flow.

### Delivery lifecycle

![Six-stage delivery lifecycle](assets/fig-03-delivery-sequence-en.svg)

1. **Request:** The customer places an order through the connected delivery platform.
2. **Assign:** The AI system determines the destination, selects an available drone, and plans the route.
3. **Navigate:** The drone uses GPS, sensors, and satellite communication while the AI system updates guidance as conditions change.
4. **Notify:** The customer receives a text or app alert approximately five minutes before arrival.
5. **Deliver:** The parcel is received at a predefined delivery point, such as a designated ground-level zone or window.
6. **Learn:** Flight paths, sensor data, and images are retained for later improvements to navigation, energy efficiency, and logistics planning.

The alert is intended to give the customer about five minutes to prepare. Parcel release and recipient verification still need detailed design.

## System design decisions and trade-offs

| Decision | Why it matters | Engineering question for implementation |
|---|---|---|
| Separate fleet control from network cooperation | Makes scheduling and communication responsibilities explicit | How are conflicting or stale commands resolved? |
| Combine central guidance with onboard sensing | Connects fleet-level decisions with obstacle-aware navigation | Which decisions remain local during a communication outage? |
| Use satellite communication | Makes the communication layer part of the delivery architecture | What coverage, latency, power, and redundancy budgets are achievable? |
| Reuse delivery data | Connects operations with subsequent model improvement | How are data quality, model validation, and release control managed? |
| Define designated delivery points | Connects navigation with the customer handoff | How is a safe delivery point confirmed before parcel release? |

I explore these implementation questions in the [system design analysis](docs/system-design.md).

## Safety, security, and learning

![Obstacle, communication, and power scenarios mapped to described responses and implementation conditions](assets/fig-05-safety-responses-en.svg)

- **Safety:** Continuous monitoring, obstacle detection and avoidance, communication redundancy, and return-to-base or safe-landing behavior in response to power or communication problems.
- **Communication:** Encryption, authentication, and quantum-resistant cryptographic protocols. Protocol selection, key management, and security testing are implementation work.
- **Data:** Images, sensor readings, and flight paths are stored in an encrypted cloud database and reused for AI improvement.
- **Evaluation priorities:** Delivery completion, route adaptation, alert timing, energy per successful delivery, communication recovery, and safety responses. The [evaluation plan](docs/system-design.md#8-evaluation-plan) defines the proposed measures and test scenarios.

<details>
<summary><strong>View the operational learning cycle</strong></summary>

![Collection, encrypted storage, and AI improvement, with proposed model evaluation and release controls](assets/fig-06-learning-flow-en.svg)

The left column shows how delivery data supports AI improvement. On the right, I outline a proposed process for validating data, evaluating models, approving updates, and monitoring their behavior. See the [system design analysis](docs/system-design.md) for details.

</details>

## Patent claims and technical traceability

The claims cover the delivery system and four supporting features. C1–C5 below are short references to the corresponding statements in the [specification](source/specification.txt).

| Claim label | Subject | Architecture element |
|---|---|---|
| C1 | Drones with GPS, sensors, and communication modules; AI-managed delivery using satellite communication | Drone fleet and AI control system |
| C2 | Hierarchical agents coordinate scheduling and routing | Fleet coordination |
| C3 | Network agents manage real-time communication between drones and customers | Network cooperation and customer interface |
| C4 | Automatic alert before arrival | Customer notification workflow |
| C5 | Operational data reused for improvements; electric-powered drones | Learning lifecycle and drone platform |

The [claim map](docs/claim-map.md) links each feature to its section in the specification.

## Applications and extensions

I also considered medical supply delivery, disaster relief logistics, and future transportation systems such as air taxis. These applications would need separate operating requirements and validation.

## Documentation

| Document | English | 日本語 |
|---|---|---|
| Portfolio overview | This page | [概要](japanese-readme.md) |
| System design and evaluation plan | [System design](docs/system-design.md) | [システム設計](docs/system-design.ja.md) |
| Claim-to-design mapping | [Claim map](docs/claim-map.md) | [請求項と設計の対応](docs/claim-map.ja.md) |
| Patent details | [Patent record](docs/patent-record.md) | [特許情報](docs/patent-record.ja.md) |
| Patent specification | [Original English text](source/specification.txt) | 英語原文を参照 |

## About the drawings

I created these diagrams to explain the system and its workflows. They are explanatory drawings, separate from the official patent documents. The [drawing index](assets/README.md) lists all six figures and their reference numbers.

No software or patent license is granted through this repository.
