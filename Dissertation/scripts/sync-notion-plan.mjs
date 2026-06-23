import "dotenv/config";
import fs from "node:fs/promises";
import { Client } from "@notionhq/client";
import { NotionToMarkdown } from "notion-to-md";

const NOTION_TOKEN = process.env.NOTION_TOKEN;
const NOTION_PAGE_ID = process.env.NOTION_PAGE_ID;

if (!NOTION_TOKEN || !NOTION_PAGE_ID) {
  console.error("Missing NOTION_TOKEN or NOTION_PAGE_ID in .env");
  process.exit(1);
}

const outputFile = "MSc Business Analytics Dissertation — Project Plan.md";

const notion = new Client({ auth: NOTION_TOKEN });
const n2m = new NotionToMarkdown({ notionClient: notion });

const mdBlocks = await n2m.pageToMarkdown(NOTION_PAGE_ID);
const mdString = n2m.toMarkdownString(mdBlocks);

const finalMarkdown = `<!-- AUTO-GENERATED FROM NOTION -->
<!-- Edit the Notion page, then run: npm run sync:notion -->

# MSc Business Analytics Dissertation — Project Plan

${mdString.parent}
`;

await fs.writeFile(outputFile, finalMarkdown, "utf8");

console.log(`Synced Notion page to: ${outputFile}`);
