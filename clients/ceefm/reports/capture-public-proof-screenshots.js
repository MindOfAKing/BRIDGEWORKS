const path = require("path");
const { chromium } = require("playwright");

const outDir = path.resolve(__dirname, "charts", "2026-04");

async function capture(page, url, filename, options = {}) {
  await page.goto(url, { waitUntil: "networkidle", timeout: 90000 });
  if (options.wait) {
    await page.waitForTimeout(options.wait);
  }
  await page.screenshot({
    path: path.join(outDir, filename),
    fullPage: options.fullPage ?? false,
  });
}

async function main() {
  const browser = await chromium.launch({
    headless: true,
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
  });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
  });
  const page = await context.newPage();

  await capture(page, "https://ceefm.eu/", "D-homepage-rendered.png", { fullPage: true });
  await capture(
    page,
    "https://securityheaders.com/?q=ceefm.eu&followRedirects=on",
    "B-security-headers-grade.png",
    { wait: 5000 }
  );
  await capture(
    page,
    "https://pagespeed.web.dev/analysis?url=https%3A%2F%2Fceefm.eu",
    "C-pagespeed-mobile-desktop.png",
    { wait: 30000 }
  );

  const llms = await (await fetch("https://ceefm.eu/llms.txt")).text();
  const robots = await (await fetch("https://ceefm.eu/robots.txt")).text();
  await page.setContent(
    `<!doctype html>
    <html>
      <head>
        <meta charset="utf-8" />
        <style>
          body { margin: 0; font-family: Arial, sans-serif; background: #F5F0E8; color: #1C2B3A; }
          .wrap { padding: 36px; display: grid; gap: 24px; }
          .panel { background: #fff; border: 1px solid #D8CFC2; border-radius: 8px; overflow: hidden; }
          .bar { background: #0F1A2E; color: #fff; padding: 14px 18px; font-weight: 700; }
          pre { margin: 0; padding: 18px; white-space: pre-wrap; font-size: 14px; line-height: 1.45; }
        </style>
      </head>
      <body>
        <div class="wrap">
          <div class="panel"><div class="bar">https://ceefm.eu/llms.txt</div><pre>${escapeHtml(llms)}</pre></div>
          <div class="panel"><div class="bar">https://ceefm.eu/robots.txt</div><pre>${escapeHtml(robots)}</pre></div>
        </div>
      </body>
    </html>`,
    { waitUntil: "load" }
  );
  await page.screenshot({ path: path.join(outDir, "H-llms-and-robots.png"), fullPage: true });

  await browser.close();
  console.log("Captured public proof screenshots in " + outDir);
}

function escapeHtml(text) {
  return text
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
