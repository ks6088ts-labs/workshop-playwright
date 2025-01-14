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
