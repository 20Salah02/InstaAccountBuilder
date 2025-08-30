const puppeteer = require("puppeteer");
const faker = require("faker");
const fs = require("fs");

async function createMailComEmail() {
    const browser = await puppeteer.launch({ headless: true }); 
    const page = await browser.newPage();

    try {
        await page.goto("https://www.mail.com/int/", { waitUntil: "networkidle2" });

        await page.waitForSelector('a[href*="signup"]', { timeout: 10000 });
        await page.click('a[href*="signup"]');
        await page.waitForTimeout(5000);

        const firstName = faker.name.firstName();
        const lastName = faker.name.lastName();
        const username = faker.internet.userName();
        const password = faker.internet.password(12);
        const email = `${username}@mail.com`;

        await page.waitForSelector('input[name="firstname"]', { timeout: 10000 });
        await page.type('input[name="firstname"]', firstName, { delay: 50 });
        await page.type('input[name="lastname"]', lastName, { delay: 50 });
        await page.type('input[name="email"]', username, { delay: 50 });
        await page.type('input[name="password"]', password, { delay: 50 });
        await page.type('input[name="passwordConfirm"]', password, { delay: 50 });

        await page.waitForSelector('select[name="domain"]', { timeout: 10000 });
        await page.select('select[name="domain"]', "mail.com");

        await page.waitForSelector('button[type="submit"]', { timeout: 10000 });
        await page.click('button[type="submit"]');
        await page.waitForTimeout(7000);

        fs.appendFileSync("mail_com_accounts.txt", `${email}:${password}\n`);
        console.log(`✅ تم إنشاء البريد: ${email}`);

    } catch (error) {
        console.error("Problem", error);
    } finally {
        await browser.close();
    }
}

(async () => {
    for (let i = 0; i < 3; i++) {
        await createMailComEmail();
    }
})();

