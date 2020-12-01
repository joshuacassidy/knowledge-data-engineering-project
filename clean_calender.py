import csv

with open('data/calendar.csv') as csvfile:
    calendar = csv.reader(csvfile, quotechar='"')
    cleanedReviews = open("cleaned_data/Calendar.csv", "w+")
    cleanedReviewsWriter = csv.writer(cleanedReviews)
    cleanedReviewsWriter.writerow(["AccommodationId", "AvailabilityId", "CalenderDate", "Available", "Price","AdjustedPrice","MinimumNights","MaximumNights"])


    # listing_id,date,available,price,adjusted_price,minimum_nights,maximum_nights
    review_id = 1
    count = 0
    for row in calendar:
        if count == 0:
            count +=1
            continue
        price, adjustedPrice, minimumNights, maximumNights = row[3].replace("$", "").replace(",", ""), row[4].replace("$", "").replace(",", ""), row[5], row[6]
        price = price if price.strip() != "" else 0
        adjustedPrice = adjustedPrice if adjustedPrice.strip() != "" else 0
        minimumNights = int(minimumNights) if minimumNights.strip() != "" else 0
        maximumNights = int(maximumNights) if maximumNights.strip() != "" else 0

        cleanedReviewsWriter.writerow([row[0], review_id, row[1], "false" if row[2] == "f" else "true", price, adjustedPrice, minimumNights, maximumNights ])
        review_id += 1
        # sample size
        if review_id >= 700:
            break
        # sample size
    cleanedReviews.close()
