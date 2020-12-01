import csv

with open('data/reviews.csv') as csvfile:
    activities = csv.reader(csvfile, quotechar='"')
    cleanedReviews = open("cleaned_data/Reviews.csv", "w+")
    cleanedReviewsWriter = csv.writer(cleanedReviews)
    cleanedReviewsWriter.writerow(["AccommodationId", "ReviewDate", "ReviewId", "ReviewerName","Comments"])

    review_id = 1
    count = 0
    for row in activities:
        if count == 0:
            count +=1
            continue
        cleanedReviewsWriter.writerow([row[0], row[2], review_id, row[3], row[4], row[5].replace("\n", "") ])
        review_id += 1
        # sample size
        if review_id >= 700:
            break
        # sample size
    cleanedReviews.close()
