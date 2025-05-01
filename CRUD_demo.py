"""Basic MongoDB operations: insert, find, update, and delete bills."""

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
collection = db["details"]

new_bill = {
    "vendor": "Amazon",
    "amount": 299.99,
    "date": "2025-04-23"
}

insert_result = collection.insert_one(new_bill)
print(f"Inserted Bill ID: {insert_result.inserted_id}")

print("\nAll bills:")
for bill in collection.find():
    print(bill)

update_result = collection.update_one({"vendor": "Amazon"}, {"$set": {"amount": 349.99}})
print(f"\nUpdated {update_result.modified_count} document(s)")

delete_result = collection.delete_one({"vendor": "Amazon"})
print(f"\nDeleted {delete_result.deleted_count} document(s)")
