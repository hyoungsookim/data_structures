
def print_star(star_count):
    #for i in range(star_count * 2):
    for i in range(star_count + 1):
        if i <= round(star_count / 2.0 + 0.5):
            space = star_count - i
            stars = (i * 2) - 1
            print(' ' * space + '*' * stars)
        else:
            #space = i - star_count
            space = i - 1
            #stars = (star_count * 2) - i
            stars = stars - 2
            print(' ' * space + '*' * stars)


if __name__ == '__main__':
    print_star(3)
    print_star(5)
    print_star(7)
