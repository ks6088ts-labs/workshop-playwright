# workshop-playwright

- [Playwright for Python > Getting Started](https://playwright.dev/python/docs/intro)
- [Playwright Trace Viewer](https://trace.playwright.dev/)

```shell
# Install dependencies
make install-deps-dev

# Run tests in verbose mode
make test-verbose

# Show traces
make show-trace

# Generate code
make codegen
```

## [Microsoft Playwright Testing](https://learn.microsoft.com/ja-jp/azure/playwright-testing/)

- [microsoft/playwright-testing-service/samples/get-started > Get Started Sample](https://github.com/microsoft/playwright-testing-service/tree/main/samples/get-started)

```shell
git clone https://github.com/microsoft/playwright-testing-service.git
cd playwright-testing-service/samples/get-started

export PLAYWRIGHT_SERVICE_URL=wss://*.api.playwright.microsoft.com/accounts/eastasia_*/browsers

# Install dependencies
npm install

# Run tests
npx playwright test --config=playwright.service.config.ts --workers=20
```

## [locust](https://docs.locust.io/en/stable/quickstart.html)

To try out Locust, run HTTP server locally and run Locust.

```shell
# Install dependencies
go install github.com/ks6088ts-labs/workshop-kubernetes@latest

# Run HTTP server
workshop-kubernetes sandbox http --port 8080
```

Run Locust and open the browser.

```shell
# Specify the failure percentage
export FLAKY_PERCENT=30

# Run locust
make locust

# Open browser to confirm that the failure percentage is almost 40% as specified above
# http://localhost:8089/
```
