CATEGORIES = [
    {"id": "html", "title": "HTML", "description": "The standard markup language for creating Web pages."},
    {"id": "css", "title": "CSS", "description": "The language we use to style an HTML document."},
    {"id": "js", "title": "JavaScript", "description": "The programming language of the Web."},
    {"id": "python", "title": "Python", "description": "A popular programming language for backend and data science."}
]

QUESTIONS = {
    "html": [
        {
            "id": 1,
            "text": "What does HTML stand for?",
            "options": [
                "Hyper Text Preprocessor",
                "Hyper Text Markup Language",
                "Hyper Tool Multi Language",
                "Hyper Text Multiple Language"
            ],
            "correct_answer": 1
        },
        {
            "id": 2,
            "text": "Choose the correct HTML element for the largest heading:",
            "options": ["<head>", "<h6>", "<h1>", "<heading>"],
            "correct_answer": 2
        },
        {
            "id": 3,
            "text": "What is the correct HTML element for inserting a line break?",
            "options": ["<br>", "<break>", "<lb>", "<Enter>"],
            "correct_answer": 0
        }
    ],
    "css": [
        {
            "id": 4,
            "text": "What does CSS stand for?",
            "options": [
                "Colorful Style Sheets",
                "Computer Style Sheets",
                "Creative Style Sheets",
                "Cascading Style Sheets"
            ],
            "correct_answer": 3
        },
        {
            "id": 5,
            "text": "Which HTML tag is used to define an internal style sheet?",
            "options": ["<script>", "<css>", "<style>", "<link>"],
            "correct_answer": 2
        },
        {
            "id": 6,
            "text": "Which property is used to change the background color?",
            "options": ["color", "bgcolor", "background-color", "bg-color"],
            "correct_answer": 2
        }
    ],
    "js": [
        {
            "id": 7,
            "text": "Inside which HTML element do we put the JavaScript?",
            "options": ["<js>", "<scripting>", "<script>", "<javascript>"],
            "correct_answer": 2
        },
        {
            "id": 8,
            "text": "Where is the correct place to insert a JavaScript?",
            "options": [
                "The <body> section",
                "Both the <head> section and the <body> section are correct",
                "The <head> section",
                "Nowhere, it goes in external files only"
            ],
            "correct_answer": 1
        },
        {
            "id": 9,
            "text": "How do you define a function in JavaScript?",
            "options": [
                "function myFunction()",
                "function:myFunction()",
                "def myFunction()",
                "function = myFunction()"
            ],
            "correct_answer": 0
        }
    ],
    "python": [
        {
            "id": 10,
            "text": "What is a correct syntax to output 'Hello World' in Python?",
            "options": [
                "echo('Hello World')",
                "print('Hello World')",
                "p('Hello World')",
                "echo 'Hello World'"
            ],
            "correct_answer": 1
        },
        {
            "id": 11,
            "text": "How do you insert a single-line comment in Python?",
            "options": [
                "// This is a comment",
                "/* This is a comment */",
                "# This is a comment",
                "-- This is a comment"
            ],
            "correct_answer": 2
        },
        {
            "id": 12,
            "text": "What is the correct file extension for Python files?",
            "options": [
                ".pyt",
                ".py",
                ".pt",
                ".python"
            ],
            "correct_answer": 1
        }
    ]
}

def get_categories():
    return CATEGORIES

def get_questions_by_category(category_id: str):
    return QUESTIONS.get(category_id, [])
