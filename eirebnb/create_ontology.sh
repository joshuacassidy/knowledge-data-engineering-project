#!/bin/bash
python3 preprocess_data/clean_activities.py
python3 preprocess_data/clean_calender.py
python3 preprocess_data/clean_listings.py
python3 preprocess_data/clean_reviews.py

java -jar ./r2rml/r2rml.jar csv-config.properties
