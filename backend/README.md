# EV Charging Load Balancer Backend

A modular, scalable Python backend for a Community EV Charging Load Balancer system with Smartcar OAuth integration.

## Project Structure

```
backend/
├── apps/
│   ├── api/                    # REST API application
│   │   ├── controllers/         # Request handlers
│   │   ├── routes/              # API route definitions
│   │   └── main.py              # FastAPI application entry point
│   ├── realtime/                # WebSocket server
│   │   ├── handlers/            # WebSocket event handlers
│   │   └── main.py              # WebSocket server entry point
│   └── workers/                 # Background workers
│       ├── scheduler/           # Slot rebalancing worker
│       ├── alerts/              # Abuse detection worker
│       └── telemetry/           # Token refresh worker
├── auth/
│   └── oauth/                   # OAuth implementations
│       ├── smartcar_oauth.py    # Smartcar OAuth flow
│       └── token_manager.py     # Token storage and refresh
├── config/                      # Configuration
│   ├── env.py                   # Environment variables
│   ├── settings.yaml            # Application settings
│   └── logging.py               # Logging configuration
├── db/
│   ├── models/                  # SQLAlchemy models
│   ├── repos/                   # Repository pattern implementations
│   └── base.py                  # Database setup
├── domain/                      # Core business logic
│   ├── charging/                # Charging session management
│   ├── fleet/                   # Fleet management
│   ├── grid/                    # Grid cluster management
│   ├── pricing/                 # Dynamic pricing
│   └── scheduling/              # Slot allocation and fairness
├── events/                      # Event system
│   ├── producers/               # Event producers
│   ├── consumers/               # Event consumers
│   └── topics.py                # Event topic definitions
├── integrations/
│   ├── chargers/                # OCPP adapter
│   └── vehicles/                # Vehicle data adapters
│       ├── smartcar_adapter.py  # Smartcar API adapter
│       └── mock_adapter.py       # Mock adapter for testing
├── monitoring/                  # Health checks and metrics
├── tests/                       # Test suite
│   ├── unit/                    # Unit tests
│   └── integration/             # Integration tests
└── requirements.txt            # Python dependencies
```

## Features

- **REST API**: FastAPI-based REST endpoints for all operations
- **WebSocket**: Real-time updates for charging progress, slot allocation, and grid alerts
- **Smartcar Integration**: OAuth flow and vehicle data retrieval
- **Slot Allocation**: Fair scheduling with priority and emergency support
- **Grid Management**: Transformer capacity management and peak shaving
- **Background Workers**: Automated slot rebalancing, token refresh, and abuse detection
- **Event System**: Pub/sub architecture for async event handling
- **Monitoring**: Health checks and metrics collection

## API Endpoints

### Authentication
- `GET /auth/smartcar/connect` - Redirect to Smartcar OAuth
- `GET /auth/smartcar/callback` - Handle OAuth callback

### Drivers
- `POST /drivers/slot/request` - Request a charging slot
- `POST /drivers/emergency/request` - Request emergency verification
- `GET /drivers/charging/status` - Get current charging session status

### Fleet
- `GET /fleet/vehicles` - Get fleet vehicle list
- `GET /fleet/vehicle/{id}` - Get vehicle details

### Grid
- `GET /grid/cluster` - Get grid cluster information

### Analytics
- `GET /analytics/fairness` - Get fairness metrics

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables**:
   Create a `.env` file with:
   ```
   DATABASE_URL=postgresql://user:password@localhost/dbname
   SMARTCAR_CLIENT_ID=your_client_id
   SMARTCAR_CLIENT_SECRET=your_client_secret
   SMARTCAR_REDIRECT_URI=http://localhost:8000/auth/smartcar/callback
   SECRET_KEY=your_secret_key
   ```

3. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

4. **Start the API server**:
   ```bash
   uvicorn apps.api.main:app --reload --port 8000
   ```

5. **Start the WebSocket server** (optional):
   ```bash
   uvicorn apps.realtime.main:app --reload --port 8001
   ```

6. **Start background workers** (optional):
   ```bash
   python apps/workers/main.py
   ```

## Development

This is a **skeleton project** with stub implementations. All methods contain `# TODO: implement logic` comments indicating where actual business logic should be implemented.

### Key Implementation Areas

1. **Domain Services**: Implement scheduling algorithms, fairness rules, and emergency verification
2. **Smartcar Integration**: Complete OAuth flow and API calls
3. **OCPP Adapter**: Implement charger communication protocol
4. **Database Logic**: Complete repository methods with actual queries
5. **Event System**: Implement pub/sub with Redis or message queue
6. **Authentication**: Add JWT token validation and user authentication

## Testing

Run tests with:
```bash
pytest tests/
```

## License

[Your License Here]
