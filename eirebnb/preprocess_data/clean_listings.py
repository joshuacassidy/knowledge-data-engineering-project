import csv
import json 

with open('data/listings.csv') as csvfile:
    listings = csv.reader(csvfile, quotechar='"')
    counties = list(csv.reader(open('cleaned_data/Counties.csv')))[1:]
    writeFileHeaderHost = [
        "hostId", "hostUrl", "hostName", 
        "hostAbout", "hostResponseTime", "hostResponseRate", "hostAcceptanceRate", 
        "hostIsSuperhost", "hostPictureUrl", "hostSince",
    ]

    cleanedHost = open("cleaned_data/Host.csv", "w")
    cleanedHostWriter = csv.writer(cleanedHost)
    cleanedHostWriter.writerow(writeFileHeaderHost)

    writeFileHeaderAccommodation = [
        "accommodationId", "hostId", "name", "description", "listingUrl", "neighborhoodOverview", "accommodates", 
        "location", "bathrooms", "bathroomsText", "bedrooms", "beds", 
        "instantBookable", "reviewsPerMonth", 
        "latitude", "longitude", "propertyTypeId", "roomTypeId", "lastUpdated"
    ]

    cleanedAccommodation = open("cleaned_data/Accommodation.csv", "w")
    cleanedAccommodationWriter = csv.writer(cleanedAccommodation)
    cleanedAccommodationWriter.writerow(writeFileHeaderAccommodation)

    writeFileHeaderAmenity = [
        "amenityId", "amenity"
    ]

    cleanedAmenity = open("cleaned_data/Amenity.csv", "w")
    cleanedAmenityWriter = csv.writer(cleanedAmenity)
    cleanedAmenityWriter.writerow(writeFileHeaderAmenity)

    writeFileHeaderAmenityJoin = [
        "accommodationId",
        "amenityId"
    ]

    cleanedAmenityJoin = open("cleaned_data/AmenityJoin.csv", "w")
    cleanedAmenityJoinWriter = csv.writer(cleanedAmenityJoin)
    cleanedAmenityJoinWriter.writerow(writeFileHeaderAmenityJoin)
    
    
    writeFileHeaderPropertyType = [
        "accommodationId", "propertyTypeId", "propertyType"
    ]

    cleanedPropertyType = open("cleaned_data/PropertyType.csv", "w")
    cleanedPropertyTypeWriter = csv.writer(cleanedPropertyType)
    cleanedPropertyTypeWriter.writerow(writeFileHeaderPropertyType)
    
    

    writeFileHeaderRoomType = [
        "accommodationId", "roomTypeId", "roomType"
    ]
    
    cleanedRoomType = open("cleaned_data/RoomType.csv", "w")
    cleanedRoomTypeWriter = csv.writer(cleanedRoomType)
    cleanedRoomTypeWriter.writerow(writeFileHeaderRoomType)
    
    writeFileHeaderAccommodationRating = [
        "accommodationRatingId", "accommodationId", "rating", "ratingAccuracy", "cleanliness", "checkin", "communication", "location", "value"
    ]

    cleanedAccommodationRating = open("cleaned_data/AccommodationRating.csv", "w")
    cleanedAccommodationRatingWriter = csv.writer(cleanedAccommodationRating)
    cleanedAccommodationRatingWriter.writerow(writeFileHeaderAccommodationRating)
    
    amenities = {}
    amenityId = 1
    count = 0
    properties = {}
    propertyId = 1
    rooms = {}
    roomId = 1
    rating_id = 1
    for i in listings:
        if count == 0:
            count += 1
            continue
        if i[30] not in properties:
            properties[i[30]] = propertyId
            cleanedPropertyTypeWriter.writerow([i[0], propertyId, i[30]])
            propertyId+=1
        if i[31] not in rooms:
            rooms[i[31]] = roomId
            cleanedRoomTypeWriter.writerow([i[0], roomId, i[31]])
            roomId+=1

  
        rating, ratingAccuracy, cleanliness, checkin, communication, location, value = i[59], i[60], i[61], i[62], i[63], i[64], i[65]
        
        rating = rating if rating.strip() != "" else 0
        ratingAccuracy = ratingAccuracy if ratingAccuracy.strip() != "" else 0
        cleanliness = cleanliness if cleanliness.strip() != "" else 0
        checkin = checkin if checkin.strip() != "" else 0
        communication = communication if communication.strip() != "" else 0
        location = location if location.strip() != "" else 0
        value = value if value.strip() != "" else 0
        
        cleanedAccommodationRatingWriter.writerow([rating_id, i[0], rating, ratingAccuracy, cleanliness, checkin, communication, location, value])
        
        for amenity in list(json.loads(i[37])):
            if amenity not in amenities:
                amenities[amenity] = amenityId
                cleanedAmenityWriter.writerow([amenityId, amenity])
                amenityId += 1
                cleanedAmenityJoinWriter.writerow([i[0], amenities[amenity]])
                
        location = i[-4]
        # print(location)
        county = None
        for j in counties:
            if j[1] in location:
                county = j[1]
                # print(county)

        hostResponseRate = int(i[16].replace("%", "") if i[16].replace("%", "").upper() != "N/A" else "0")
        hostAcceptanceRate = int(i[17].replace("%", "") if i[17].replace("%", "").upper() != "N/A" else "0")
        hostIsSuperhost = "false" if i[18] == "f" else "true"
        description = ' '.join(i[14].replace("\n", " ").split())
        
        cleanedHostWriter.writerow([
            i[9], i[10], i[11], description, 
            i[15], hostResponseRate, hostAcceptanceRate, 
            hostIsSuperhost, i[20], i[12] 
        ])

        
        accommodates, bathrooms, bedrooms, beds, reviewsPerMonth = i[32], i[33], i[35], i[36], i[79]    
        accommodates = accommodates if accommodates.strip() != "" else 0
        bathrooms = bathrooms if bathrooms.strip() != "" else 0
        bedrooms = bedrooms if bedrooms.strip() != "" else 0
        beds = beds if beds.strip() != "" else 0
        reviewsPerMonth = reviewsPerMonth if reviewsPerMonth.strip() != "" else 0
        

        cleanedAccommodationWriter.writerow([
            i[0], i[9], i[5], i[6], i[1], i[7], i[32], 
            county, i[33], i[34], i[35], i[36], 
            "false" if i[68] == "f" else "true", i[79], i[28], i[29], propertyId, roomId, i[4],
        ])

        rating_id += 1
        # sample size
        if count >= 700:
            break
        # sample size
        count +=1
        # break
