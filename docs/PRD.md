# Product Requirements Document (PRD)

## Smart Community EV Charging Management Platform

---

## 1. Purpose

This PRD defines the technical and product requirements for a software platform that coordinates EV charging across community hubs, verifies emergency and fleet priority using telemetry and identity, enforces grid limits, and provides dashboards for operators and utilities.

The document focuses on:

* API architecture
* Data models and schemas
* Backend services
* UX flows
* Fleet/OEM integrations
* Scheduling and load control

---

## 2. System Goals

* Fair scheduling for all users
* Verified priority for emergency and fleet vehicles
* Peak load shaving and transformer protection
* Integration with chargers using OCPP
* Integration with fleet/OEM systems using OAuth + APIs
* Auditability and abuse prevention
* Scalable to city-level deployments

---

## 3. High-Level Architecture

```
Mobile App / Kiosk / Web
        │
        ▼
API Gateway ────────────────┐
        │                   │
Auth Service           Operator Dashboard
        │
Scheduler & Priority Engine
        │
Load Controller / Grid Manager
        │
OCPP Charger Network

Fleet / OEM APIs ──▶ Integration Service
Utility Grid APIs ─▶
```

---

## 4. Core Backend Services

### 4.1 API Gateway

* Single entry point for all clients
* JWT-based auth tokens
* Rate limiting and logging
* Routes traffic to internal services

---

### 4.2 Auth & Identity Service

Handles:

* User accounts
* Enterprise accounts
* OAuth federation with fleet/OEM systems
* Token issuance

Supports:

* OAuth2 / OpenID Connect
* API key auth for enterprises

---

### 4.3 Scheduler & Priority Engine

Responsibilities:

* Maintain charging queues
* Compute fairness scores
* Assign priority tiers
* Generate charging schedules
* Re-balance when new vehicles arrive

Inputs:

* Charger availability
* Vehicle SOC
* Priority tier
* Grid limits
* Historical usage

---

### 4.4 Load Controller

* Enforces site power caps
* Throttles or boosts chargers
* Issues OCPP commands
* Handles transformer limits

---

### 4.5 Integration Service

Adapters for:

* Fleet telematics APIs
* OEM vehicle APIs
* Utility load forecasts

Handles:

* OAuth token refresh
* Polling/webhooks
* Data normalization

---

### 4.6 Audit & Compliance Service

* Stores immutable logs
* Priority usage tracking
* Admin investigations
* Regulatory exports

---

## 5. API Architecture

All APIs are REST/JSON initially, gRPC for internal services.

---

### 5.1 Public APIs (Client-Facing)

#### Request Charging Session

```
POST /api/v1/sessions/request
{
  "vehicle_id": "VIN123",
  "target_soc": 80,
  "time_constraint_minutes": 90
}
```

---

#### Request Urgent Review

```
POST /api/v1/sessions/{id}/urgent-review
```

---

#### Session Status

```
GET /api/v1/sessions/{id}
```

---

### 5.2 Operator APIs

* Configure grid caps
* View queues
* Approve enterprises

```
POST /api/v1/sites/{id}/grid-limit
```

---

### 5.3 Enterprise OAuth Callback

```
POST /api/v1/oauth/fleet/callback
```

---

## 6. Database Design (Core Tables)

Relational DB for transactions + time-series DB for telemetry.

---

### Users

```
id (PK)
role (driver, enterprise_admin, operator)
email
hashed_password
created_at
```

---

### Enterprises

```
id
name
type
verification_status
domain
```

---

### Vehicles

```
vin (PK)
enterprise_id (nullable)
owner_user_id
priority_eligible (bool)
```

---

### ChargingSites

```
id
location
max_kw
```

---

### Chargers

```
id
site_id
ocpp_id
max_kw
status
```

---

### Sessions

```
id
vehicle_vin
charger_id
state
priority_tier
requested_soc
assigned_start
assigned_end
```

---

### TelemetryEvents

```
id
vehicle_vin
type
value
timestamp
```

---

### PriorityAudit

```
id
vehicle_vin
soc
location_zone
decision
reason
created_at
```

---

## 7. Fleet / OEM API Integration

### 7.1 OAuth Flow

1. Enterprise clicks "Connect Fleet System"
2. Redirect to fleet/OEM auth page
3. User grants telemetry scope
4. Platform stores refresh token
5. Integration Service fetches vehicle data

---

### 7.2 Required Scopes

* vehicle.read
* battery.read
* charging.status
* mission.status (fleet only)

---

### 7.3 Polling & Webhooks

* Poll SOC every 60–120s
* Webhooks for state change

---

### 7.4 Normalization Layer

All OEM formats mapped into:

```
{
  soc,
  range_km,
  plugged_in,
  mission_active,
  gps,
  timestamp
}
```

---

## 8. Charger Control (OCPP)

* OCPP 1.6J / 2.0.1
* Start/StopTransaction
* SetChargingProfile
* MeterValues

Load Controller translates schedules into charging profiles.

---

## 9. UX Flows

### 9.1 Private Driver

* Login
* See chargers + ETA
* Request session
* Optional urgent review
* Notifications
* Session complete

---

### 9.2 Fleet Operator

* OAuth connect
* View fleet status
* Mark vehicle for priority
* Track sessions

---

### 9.3 Utility / Site Operator

* Real-time load
* Queues
* Grid caps
* Alerts
* Reports

---

## 10. Scheduling Logic (High Level)

Inputs:

* Grid cap
* Charger capacity
* Priority tier
* Fairness score

Algorithm:

1. Reserve capacity for P0/P1
2. Allocate remaining power
3. Throttle lowest fairness score first
4. Recompute every 30–60 seconds

---

## 11. Security & Privacy

* TLS everywhere
* Token encryption
* Minimal telemetry retention
* RBAC roles
* Audit trails

---

## 12. Deployment Model

* Kubernetes-based microservices
* Message bus for telemetry
* Edge gateway at charging site
* Cloud scheduler

---

## 13. MVP Scope

* Charger OCPP integration
* Rule-based scheduler
* Simulated OEM APIs
* Enterprise onboarding
* Operator dashboard

---

## 14. Phase-2 Expansion

* Live OEM integrations
* ML-based demand prediction
* Utility forecasting
* Dynamic pricing

---

**End of PRD**
