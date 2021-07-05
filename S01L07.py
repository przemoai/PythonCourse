colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def draw(colors,n):
    newColors = colors[:n]

    return newColors



for i in range(len(colors)+1):
    print(draw(colors,i))


korporacja = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'

print(korporacja[korporacja.index('(')+1:korporacja.index(')')+1])