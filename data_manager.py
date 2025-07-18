#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import logging
from typing import Dict, List, Any
from datetime import datetime
from config import APPLICATIONS_FILE, USERS_FILE, STATS_FILE

logger = logging.getLogger(__name__)

class DataManager:
    """Handle data persistence for the bot."""
    
    def __init__(self):
        self.applications = self._load_json(APPLICATIONS_FILE, [])
        self.users = self._load_json(USERS_FILE, {})
        self.stats = self._load_json(STATS_FILE, {})
    
    def _load_json(self, filename: str, default_value: Any) -> Any:
        """Load JSON data from file."""
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    return json.load(file)
            return default_value
        except Exception as e:
            logger.error(f"Failed to load {filename}: {e}")
            return default_value
    
    def _save_json(self, filename: str, data: Any) -> bool:
        """Save data to JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            logger.error(f"Failed to save {filename}: {e}")
            return False
    
    def has_user_applied(self, user_id: int, team_id: str) -> bool:
        """Check if user has already applied to a specific team."""
        for application in self.applications:
            if (application['user_info']['user_id'] == user_id and 
                application['selected_team'] == team_id):
                return True
        return False
    
    def save_application(self, application_data: dict) -> bool:
        """Save a new application."""
        try:
            # Add application to list
            self.applications.append(application_data)
            
            # Update user data
            user_id = str(application_data['user_info']['user_id'])
            if user_id not in self.users:
                self.users[user_id] = {
                    'first_name': application_data['user_info']['first_name'],
                    'last_name': application_data['user_info']['last_name'],
                    'username': application_data['user_info']['username'],
                    'first_seen': application_data['timestamp'],
                    'applications': []
                }
            
            # Add this application to user's applications
            self.users[user_id]['applications'].append({
                'team_id': application_data['selected_team'],
                'team_name': application_data['team_name'],
                'timestamp': application_data['timestamp']
            })
            
            # Update last activity
            self.users[user_id]['last_active'] = application_data['timestamp']
            
            # Save to files
            self._save_json(APPLICATIONS_FILE, self.applications)
            self._save_json(USERS_FILE, self.users)
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to save application: {e}")
            return False
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get application statistics."""
        try:
            # Count applications by team
            team_counts = {}
            unique_users = set()
            
            for application in self.applications:
                team_id = application['selected_team']
                team_counts[team_id] = team_counts.get(team_id, 0) + 1
                unique_users.add(application['user_info']['user_id'])
            
            return {
                'total_applications': len(self.applications),
                'total_users': len(unique_users),
                'team_counts': team_counts
            }
            
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
            return {
                'total_applications': 0,
                'total_users': 0,
                'team_counts': {}
            }
    
    def get_user_applications(self, user_id: int) -> List[Dict[str, Any]]:
        """Get all applications for a specific user."""
        user_applications = []
        for application in self.applications:
            if application['user_info']['user_id'] == user_id:
                user_applications.append(application)
        return user_applications
    
    def get_team_applications(self, team_id: str) -> List[Dict[str, Any]]:
        """Get all applications for a specific team."""
        team_applications = []
        for application in self.applications:
            if application['selected_team'] == team_id:
                team_applications.append(application)
        return team_applications
    
    def clear_applications(self) -> bool:
        """Clear all applications data."""
        try:
            # Clear applications and users data
            self.applications = []
            self.users = {}
            
            # Save empty data to files
            self._save_json(APPLICATIONS_FILE, self.applications)
            self._save_json(USERS_FILE, self.users)
            
            return True
        except Exception as e:
            logger.error(f"Failed to clear applications: {e}")
            return False
