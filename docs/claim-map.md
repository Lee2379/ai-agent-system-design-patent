# Claim-to-design map

[Portfolio](../README.md) · English | [日本語](claim-map.ja.md)

## Claims and design

I use C1–C5 to refer to the five claim statements in the [specification](../source/specification.txt). The table links each statement to the relevant design elements. It is a technical summary; the patent documents define the claims.

## Claim summary

| Label | Subject | Supporting description | Design element |
|---|---|---|---|
| **C1** | One or more drones with GPS, sensors, and communication modules; AI agents manage autonomous delivery using satellite communication | Summary of the Invention; Detailed Description → System Architecture and Communication Framework | AI control system, communication layer, and autonomous drone fleet |
| **C2** | Hierarchical agents coordinate drone scheduling and routing | Summary of the Invention; System Architecture; AI Agent Operation | Hierarchical-agent responsibility table and route/assignment stage |
| **C3** | Network agents manage real-time communication between drones and customers | Summary of the Invention; Communication Framework | Network-agent responsibility table and status/notification interactions |
| **C4** | AI sends an automatic delivery alert before arrival | System Operation, step 4; Product Delivery Process, step 3 | Pre-arrival notification stage; description gives approximately five minutes |
| **C5** | Operational data are reused for future improvement and drones use electric power | System Operation, step 6; Key Advantages; Learning and Optimization | Operational data lifecycle and electric drone platform |

## Description details beyond the five claim summaries

The detailed description also covers the following features.

| Feature | Where described | How it is presented here |
|---|---|---|
| Camera images and encrypted cloud storage | System Architecture; Learning and Optimization | Data collection and storage |
| Deep learning for routing and obstacle avoidance | AI Agent Operation | Deep learning; model architecture and training procedures remain to be defined |
| Encrypted, authenticated, quantum-resistant communication | Communication Framework | Security requirements; protocol selection and testing remain implementation work |
| Redundant communication and emergency return/landing | Safety Considerations | Safety behavior and conditions to resolve during implementation |
| Ground-level zones or designated windows | System Operation, step 5 | Delivery-point options; parcel release requires detailed design |
| Medical logistics, disaster response, and air taxis | Applications and Extensions | Proposed application directions |

## Related documents

The [system design analysis](system-design.md) explores implementation choices and evaluation methods beyond the patent description. The [patent details](patent-record.md) list the registration information and supporting files.
