const puppeteer = require('puppeteer');
const faker = require('faker');
const axios = require('axios');

async function createTempEmail() {
  try {
    const response = await axios.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox', {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      }
    });
    return response.data[0];
  } catch (error) {
    console.log('فشل إنشاء البريد:', error.message);
    return null;
  }
}

async function getEmailCode(email) {
  try {
    const [user, domain] = email.split('@');
    let attempts = 0;

    while (attempts < 10) {
      const response = await axios.get(`https://www.1secmail.com/api/v1/?action=getMessages&login=${user}&domain=${domain}`);
      
      if (response.data.length > 0) {
        const messageId = response.data[0].id;
        const messageRes = await axios.get(`https://www.1secmail.com/api/v1/?action=readMessage&login=${user}&domain=${domain}&id=${messageId}`);
        
        if (/(\d{6})/.test(messageRes.data.textBody)) {
          return messageRes.data.textBody.match(/(\d{6})/)[1];
        }
      }
      
      await new Promise(resolve => setTimeout(resolve, 5000));
      attempts++;
    }
    
    return null;
  } catch (error) {
    console.log('فشل استلام الرمز:', error.message);
    return null;
  }
}

async function createAccount() {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  try {
    const email = await createTempEmail();
    if (!email) return;

    await page.goto('https://www.instagram.com/accounts/emailsignup/');
    await page.waitForTimeout(2000);

    await page.type('input[name="emailOrPhone"]', email);
    await page.type('input[name="fullName"]', faker.name.findName());
    await page.type('input[name="username"]', faker.internet.userName() + faker.datatype.number(999));
    await page.type('input[name="password"]', faker.internet.password(12));
    await page.click('button[type="submit"]');
    
    await page.waitForSelector('select[title="Year"]');
    await page.select('select[title="Day"]', String(faker.datatype.number({min:1, max:28})));
    await page.select('select[title="Month"]', String(faker.datatype.number({min:1, max:12})));
    await page.select('select[title="Year"]', String(faker.datatype.number({min:1990, max:2000})));
    await page.click('button[type="submit"]');
    
    await page.waitForSelector('input[name="email_confirmation_code"]');
    const code = await getEmailCode(email);
    
    if (code) {
      await page.type('input[name="email_confirmation_code"]', code);
      await page.click('button[type="submit"]');
      await page.waitForTimeout(5000);
      console.log(' تم إنشاء الحساب بنجاح!');
    } else {
      console.log(' فشل التحقق من البريد');
    }

  } catch (error) {
    console.log('حدث خطأ:', error.message);
  } finally {
    await browser.close();
  }
}

// التشغيل
(async () => {
  await createAccount();
})();