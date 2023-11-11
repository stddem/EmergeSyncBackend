from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException
from bson.objectid import ObjectId
from pydantic import BaseModel
from typing import Optional

class Profile(BaseModel):
    first_name: str
    middle_name: str
    last_name: str

class ProfileController:
    def __init__(self, database_url: str, database_name: str = "EmergeSync"):
        self.client = AsyncIOMotorClient(database_url)
        self.db = self.client[database_name]
        self.profile_collection = self.db["profile"]

    async def create_profile(self, user_id:str, profile: Profile):
        profile_doc = profile.dict()
        result = await self.profile_collection.insert_one(profile_doc)
        return str(result.inserted_id)

    async def get_profile(self, profile_id: str) -> Optional[Profile]:
        profile = await self.profile_collection.find_one({"_id": ObjectId(profile_id)})
        return Profile(**profile) if profile else None 
      
    async def change_profile(self, profile_id: str, updated_profile: Profile):
      existing_profile = await self.profile_collection.find_one({"_id": ObjectId(profile_id)})
      if not existing_profile:
          raise HTTPException(status_code=404, detail="Profile not found")
      
      await self.profile_collection.update_one(
          {"_id": ObjectId(profile_id)},
          {"$set": updated_profile.dict(exclude_unset=True)}
      )
      return {"message": "Profile updated successfully"}
    
                                                                                                                                                                                                                                              