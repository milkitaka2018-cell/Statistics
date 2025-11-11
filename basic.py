text = "The sun dipped below the horizon, painting the sky in vibrant shades of orange and purple. A gentle breeze rustled the leaves of the ancient oak trees, creating a soft, whispering sound. In the distance, the lights of the small town began to twinkle like scattered stars. The evening air grew cool, carrying the scent of damp earth and night-blooming flowers. It was a moment of perfect, serene tranquility at the end of the day."
for sentence in text.split("."):
    for word in sentence.split():
        print(sentence[-1])
