from faker import Faker
import pandas as pd

fake = Faker()
domains = ["domain1.com", "domain2.com", "domain3.com", "domain4.com", "domain5.com", 
           "domain6.com", "domain7.com", "domain8.com", "domain9.com", "domain10.com"]

emails = []
for i in range(10000):
    email = f"{fake.first_name().lower()}{fake.random_int(100, 999)}@{domains[i % 10]}"
    password = fake.password(length=12)
    emails.append([email, password])

# حفظ البيانات في CSV
df = pd.DataFrame(emails, columns=["Email", "Password"])
df.to_csv("emails.csv", index=False)

print("✅ تم إنشاء 10,000 بريد وحفظها في emails.csv")


