def book_discovery_system():

    book= [
        {"title": "Maha Prasthanam", "genre": "Poetry", "rating": 4.9},
        {"title": "Kanyasulkam", "genre": "Drama", "rating": 4.8},
        {"title": "Veyi Padagalu", "genre": "Novel", "rating": 4.8},
        {"title": "Asamardhuni Jeeva Yatra", "genre": "Novel", "rating": 4.7},
        {"title": "Chivaraku Migiledi", "genre": "Novel", "rating": 4.6},
        {"title": "Barrister Parvateesam", "genre": "Comedy", "rating": 4.9},
        {"title": "Ganapathi", "genre": "Comedy", "rating": 4.5},
        {"title": "Amaravati Kathalu", "genre": "Stories", "rating": 4.8},
        {"title": "Galivana", "genre": "Stories", "rating": 4.6},
        {"title": "Maidanam", "genre": "Romance", "rating": 4.7},
        {"title": "Prema Lekhalu", "genre": "Romance", "rating": 4.5},
        {"title": "Srikrishna Rayabaram", "genre": "Mythology", "rating": 4.9},
        {"title": "Andhra Mahabharatam", "genre": "Mythology", "rating": 4.8},
        {"title": "Buddhuni Jeevitam", "genre": "Biography", "rating": 4.6},
        {"title": "APJ Abdul Kalam Jeevita Charitra", "genre": "Biography", "rating": 4.8}
    ]

    print("=" * 60)
    print("      TELUGU BOOK RECOMMENDATION SYSTEM")
    print("=" * 60)

    genres = sorted(set(book["genre"] for book in book))

    while True:

        print("\nAvailable Genres:")
        for genre in genres:
            print("-", genre)

        genre_choice = input(
            "\nEnter your preferred genre: "
        ).title().strip()

        if genre_choice not in genres:
            print("\nSorry! Genre not available.")
            continue

        try:
            min_rating = float(
                input("Enter minimum rating (1.0 - 5.0): ")
            )
        except ValueError:
            print("\nPlease enter a valid rating.")
            continue

        print("\nRecommended Telugu Books:\n")

        found = False

        for book in book:
            if (book["genre"] == genre_choice and
                    book["rating"] >= min_rating):

                print(
                    f"📚 {book['title']} "
                    f"(Rating: {book['rating']}/5)"
                )
                found = True

        if not found:
            print("No books found matching your criteria.")

        continue_choice = input(
            "\nDo you want more recommendations? (yes/no): "
        ).lower().strip()

        if continue_choice != "yes":
            print(
                "\nThank you for using the Telugu Book "
                "Recommendation System!"
            )
            break


book_discovery_system()
