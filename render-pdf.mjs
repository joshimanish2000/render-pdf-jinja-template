import puppeteer from "puppeteer";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const browser = await puppeteer.launch({ headless: true });
const page = await browser.newPage();
await page.goto(`file://${__dirname}/report.html`);
await page.pdf({ path: "report.pdf" });

await browser.close();
