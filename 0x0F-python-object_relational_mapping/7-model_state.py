#!/usr/bin/python3


"""
Module to list all state objects from the database
"""
if __name__ == "__main__":
	from sqlalchemy import create_engine
	from sqlalchemy.ext.declarative import declarative_base


	Base = declarative_base()


	