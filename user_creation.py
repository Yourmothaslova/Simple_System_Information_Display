#!/usr/bin/env python3
import os
import subprocess

username = input("Please enter the name of the user you wish to create: ")

def create_user(username):
	try:
		subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", username], check=True)
		print(f"User {username} created successfully")
	except subprocess.CalledProcessError:
		print(f"Failed to create user {username}.")

create_user(username)
