def word_frequency(text): 
    words = text.lower().split()  # Chuyển về chữ thường và tách thành từ
    total_words = len(words)  # Tính tổng số từ
    counts = {}  # Khởi tạo dictionary để đếm tần suất từ

    # Đếm tần suất của mỗi từ
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    # Sắp xếp các từ theo tần suất giảm dần và lấy top 5
    sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
    top_5 = dict(sorted_words)
    
    # Tổng tần suất của top 5 từ
    sum_top_5 = sum(top_5.values())
    # Tính tỷ lệ phần trăm của top 5 từ so với tổng số từ
    proportion = (sum_top_5 / total_words) * 100

    # In tất cả thông tin cần thiết
    print("Top 5:", top_5)
    print("Total words:", total_words)
    print("Proportion:", sum_top_5, "/", total_words, "=", round(proportion, 2), "%")

# Nhập văn bản từ người dùng
text_input = input("Enter your text here: ")
word_frequency(text_input)