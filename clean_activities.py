import csv

with open('data/Activities.csv') as csvfile:
    activities = csv.reader(csvfile, quotechar='"')
    cleanedActivitiesTypes = open("cleaned_data/ActivitiesTypes.csv", "w+")
    cleanedActivitiesTypesWriter = csv.writer(cleanedActivitiesTypes)
    cleanedActivitiesTypesWriter.writerow(["ActivityTypeID","ActivityType"])

    cleanedActivities = open("cleaned_data/Activities.csv", "w+")
    cleanedActivitiesWriter = csv.writer(cleanedActivities)
    cleanedActivitiesWriter.writerow(["ActivityID", "Name","Url","Telephone","Longitude","Latitude","AddressRegion","AddressLocality","AddressCountry"])
    
    cleanedActivitiesJoin = open("cleaned_data/ActivitiesJoin.csv", "w+")
    cleanedActivitiesJoinWriter = csv.writer(cleanedActivitiesJoin)
    cleanedActivitiesJoinWriter.writerow(["ActivityID", "ACTIVITYTYPEID"])
    
    counties = open("cleaned_data/Counties.csv", "w+")
    countiesWriter = csv.writer(counties)
    countiesWriter.writerow(["Country", "County", "isCapital"])

    activityCounties = {}
    activitiesTypes = {}
    count = 0
    activityId = 1
    activityTypesId = 1
    for row in activities:
        if count == 0:
            count +=1
            continue
        if row[5] not in activityCounties and row[5].strip(' ') != "":
            activityCounties[row[5]] = row[5]
            countiesWriter.writerow([row[7],activityCounties[row[5]], "true" if row[5].strip() == "Dublin" else "false" ])
        
        # print(row)
        write_row = row[0:len(row)-1]
        write_row.insert(0, activityId)
        activityID, name, url, telephone, longitude, latitude, addressRegion, addressLocality, addressCountry = write_row

        
        cleanedActivitiesWriter.writerow([activityID, name, url, telephone, longitude, latitude, addressRegion, addressLocality, addressCountry])
        for activityType in row[-1].split(","):
            
            if activityType not in activitiesTypes:
                cleanedActivitiesTypesWriter.writerow([activityTypesId, activityType])
                activitiesTypes[activityType] = activityTypesId
            
            cleanedActivitiesJoinWriter.writerow([activityId, activitiesTypes[activityType]])
            activityTypesId += 1
        
        # sample size
        if count >= 700:
            break
        # sample size
        activityId += 1
        count +=1
    cleanedActivities.close()
