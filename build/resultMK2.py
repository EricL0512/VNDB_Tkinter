import requests
from build.tag import Tag
import selection

name_str = ''
developer_str = ''
rating_str = ''
greater_than = True
less_than = False


def rating_format_helper():
    if len(rating_str) <= 1:
        return False
    return True

def rating_format():
    temp = ['rating', '>=', '11']
    if less_than:
        temp.pop(1)
        temp.insert(1, '<=')
    temp.pop(2)
    temp.append(rating_str)
    return temp


def filter_format():
    filters = ['and', ["search", "=", name_str], ['developer', '=', ['search', '=', developer_str]], ["id", ">=", "v1"] ]
    if rating_format_helper():
        filters.append(rating_format())
    if tags_lib['FANTASY'] % 3 == 1: # this was made at 4 AM. Forgive me...
        filters.append(['tag', '=', Tag.FANTASY.value])
    if tags_lib['FANTASY'] % 3 == 2:
        filters.append(['tag', '!=', Tag.FANTASY.value])
    if tags_lib['DRAMA'] % 3 == 1:
        filters.append(['tag', '=', Tag.DRAMA.value])
    if tags_lib['DRAMA'] % 3 == 2:
        filters.append(['tag', '!=', Tag.DRAMA.value])
    if tags_lib['ROMANCE'] % 3 == 1:
        filters.append(['tag', '=', Tag.ROMANCE.value])
    if tags_lib['ROMANCE'] % 3 == 2:
        filters.append(['tag', '!=', Tag.ROMANCE.value])
    if tags_lib['SEXUAL_CONTENT'] % 3 == 1:
        filters.append(['tag', '=', Tag.SEXUAL_CONTENT.value])
    if tags_lib['SEXUAL_CONTENT'] % 3 == 2:
        filters.append(['tag', '!=', Tag.SEXUAL_CONTENT.value])
    if tags_lib['SCIENCE_FICTION'] % 3 == 1:
        filters.append(['tag', '=', Tag.SCIENCE_FICTION.value])
    if tags_lib['SCIENCE_FICTION'] % 3 == 2:
        filters.append(['tag', '!=', Tag.SCIENCE_FICTION.value])
    if tags_lib['COMEDY'] % 3 == 1:
        filters.append(['tag', '=', Tag.COMEDY.value])
    if tags_lib['COMEDY'] % 3 == 2:
        filters.append(['tag', '!=', Tag.COMEDY.value])
    if tags_lib['MYSTERY'] % 3 == 1:
        filters.append(['tag', '=', Tag.MYSTERY.value])
    if tags_lib['MYSTERY'] % 3 == 2:
        filters.append(['tag', '!=', Tag.MYSTERY.value])
    if tags_lib['HORROR'] % 3 == 1:
        filters.append(['tag', '=', Tag.HORROR.value])
    if tags_lib['HORROR'] % 3 == 2:
        filters.append(['tag', '!=', Tag.HORROR.value])
    if tags_lib['ACTION'] % 3 == 1:
        filters.append(['tag', '=', Tag.ACTION.value])
    if tags_lib['ACTION'] % 3 == 2:
        filters.append(['tag', '!=', Tag.ACTION.value])
    return filters


def remove_square_brackets(input_string, start=0):
    if input_string is None:
        return ""

    opening_bracket = input_string.find('[', start)
    if opening_bracket == -1:
        return input_string

    closing_bracket = input_string.find(']', opening_bracket)
    if closing_bracket == -1:
        return input_string

    result = input_string[:opening_bracket] + input_string[closing_bracket + 1:]
    return remove_square_brackets(result, opening_bracket)

# Example of what a proper filter would look like
# ['and'
#     , ["search", "=", "Clannad"]
#     , ['developer', '=', ['search', '=', 'Key']]  # These three must be true
#     , ["id", ">=", "v1"]  # placeholder
#     , ['tag', '!=', [Tag.ROMANCE.value, 0, 0]]  # as long as one of them are true
#     , ["rating", ">", "70"]
#  ]
def main(tags_lib1, name_str1 = '', developer_str1 = '', rating_str1 = '', greater_than1 = True, less_than1 = False) -> None:
    global tags_lib
    global name_str
    global developer_str
    global rating_str
    global greater_than
    global less_than
    tags_lib = tags_lib1
    name_str = name_str1
    developer_str = developer_str1
    rating_str = rating_str1
    greater_than = greater_than1
    less_than = less_than1
    url = "https://api.vndb.org/kana/vn"
    headers = {"Content-Type": "application/json"}
    data = {
        "fields": "title, image.url, rating, tags.name, developers.name, length_minutes, votecount, description",
        "filters": filter_format(),
        "sort": "votecount",
        "reverse": True, # Normally sorts from lowest to highest
        "results": 10
    }
    response = requests.post(url, headers=headers, json=data)
    result_json = response.json()

    for i in result_json['results']:
        print("\033[31m****************************************************************************************************************************************************************************************\033[0m")
        print("Title: " + i['title'])
        print("Rating: " + str(i['rating']) + " / 100")
        print("Number of Votes: " + str(i['votecount']))
        print("Image URL: " + i['image']['url'])
        print("Developers: ", end='')
        for j in i['developers']:
            print(j['name'], end=', ')
        print('\n')
        print("Tags: ")
        for j in i['tags']:
            print(j['name'], end=', ')
        print('\n')
        print("Description:")
        print(remove_square_brackets(i['description']))


if __name__ == '__main__':
    main()