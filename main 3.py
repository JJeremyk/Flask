print("hello")
def add_question():
    questions = [
        ('How many months in a year have 28 days?','All','One','None','Two'),
        ('What will the green cliff look like if it falls into the Red Sea?','Wet','Red','Will not change','Purple'),
        ('Which hand is better to stir tea with?','With a spoon','Right','Left','Any'),
        ('What has no length, depth, width or height,but can be measured?','Time','Stupidity','The sea','Air'),
        ('When is it possible to draw out water with a net?','When the water is frozen','When there are no fish','When the goldfish swim away','When the net breaks'),
        ('What is bigger than an elephant and weighs nothing?','Shadow of elephant','A balloon','A parachute','A cloud')
    ]
    open()
    cursor.executemany('''INSERT INTO question (question, answers, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''',questions)
    conn.commit()
    close()

def add_quiz():
    quizes = [
        ('own game',),
        ('Who wants to be a millionare?',),
        ('The smartest',)
    ]
    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()

def add_links():
    open()
    cursor.execute('''PRAGMA foreign_keys = on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
    answer = input("Add a link (y/n)?")
    while answer != 'n':
        quiz_id = int(input("quiz id: "))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
        answer = input('Add link (y/n)?')
    close()