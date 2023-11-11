from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from pydantic import BaseModel
from typing import Optional
from controllers.profile_controller import ProfileController, Profile

class User(BaseModel):
    username: str
    password: str

class UserController:
    def __init__(self, database_url: str, database_name: str = "EmergeSync"):
        self.client = AsyncIOMotorClient(database_url)
        self.db = self.client[database_name]
        self.users_collection = self.db["users"]
        self.database_url = database_url

    async def create_user(self, user: User):
        user_doc = user.dict()
        result = await self.users_collection.insert_one(user_doc)
        
        profile_data = {"first_name":"", "middle_name":"", "last_name":""}
        
        profile_controller = ProfileController(self.database_url)
        await profile_controller.create_profile(profile, result.inserted_id)
        
        return str(result.inserted_id)

    async def get_user(self, user_id: str) -> Optional[User]:
        user = await self.users_collection.find_one({"_id": ObjectId(user_id)})
        return User(**user) if user else None

    async def get_user_by_username(self, username: str) -> Optional[str]:
        user = await self.users_collection.find_one({"username": username})
        return str(user["_id"]) if user else None
    
