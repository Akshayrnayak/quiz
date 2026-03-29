CATEGORIES = [
    {"id": "html", "title": "HTML", "description": "The standard markup language for creating Web pages."},
    {"id": "css", "title": "CSS", "description": "The language we use to style an HTML document."},
    {"id": "js", "title": "JavaScript", "description": "The programming language of the Web."},
    {"id": "python", "title": "Python", "description": "A popular programming language for backend and data science."},
    {"id": "react", "title": "React", "description": "A JavaScript library for building user interfaces."},
    {"id": "vue", "title": "Vue.js", "description": "The Progressive JavaScript Framework."},
    {"id": "node", "title": "Node.js", "description": "JavaScript runtime built on Chrome's V8 JavaScript engine."},
    {"id": "ts", "title": "TypeScript", "description": "Strongly typed programming language that builds on JavaScript."},
    {"id": "sql", "title": "SQL", "description": "Standard language for storing, manipulating and retrieving data in databases."},
    {"id": "mongodb", "title": "MongoDB", "description": "A document-based, distributed database built for modern developers."},
    {"id": "graphql", "title": "GraphQL", "description": "A query language for your API."},
    {"id": "git", "title": "Git", "description": "A free and open source distributed version control system."},
    {"id": "docker", "title": "Docker", "description": "Platform designed to help developers build, share, and run modern applications."},
    {"id": "nextjs", "title": "Next.js", "description": "The React Framework for the Web."}
]

QUESTIONS = {
    "html": [
        {"id": 1, "text": "What does HTML stand for?", "options": ["Hyper Text Preprocessor", "Hyper Text Markup Language", "Hyper Tool Multi Language", "Hyper Text Multiple Language"], "correct_answer": 1},
        {"id": 2, "text": "Choose the correct HTML element for the largest heading:", "options": ["<head>", "<h6>", "<h1>", "<heading>"], "correct_answer": 2},
        {"id": 3, "text": "What is the correct HTML element for inserting a line break?", "options": ["<br>", "<break>", "<lb>", "<Enter>"], "correct_answer": 0}
    ],
    "css": [
        {"id": 4, "text": "What does CSS stand for?", "options": ["Colorful Style Sheets", "Computer Style Sheets", "Creative Style Sheets", "Cascading Style Sheets"], "correct_answer": 3},
        {"id": 5, "text": "Which HTML tag is used to define an internal style sheet?", "options": ["<script>", "<css>", "<style>", "<link>"], "correct_answer": 2},
        {"id": 6, "text": "Which property is used to change the background color?", "options": ["color", "bgcolor", "background-color", "bg-color"], "correct_answer": 2}
    ],
    "js": [
        {"id": 7, "text": "Inside which HTML element do we put the JavaScript?", "options": ["<js>", "<scripting>", "<script>", "<javascript>"], "correct_answer": 2},
        {"id": 8, "text": "Where is the correct place to insert a JavaScript?", "options": ["The <body> section", "Both the <head> section and the <body> section are correct", "The <head> section", "Nowhere, it goes in external files only"], "correct_answer": 1},
        {"id": 9, "text": "How do you define a function in JavaScript?", "options": ["function myFunction()", "function:myFunction()", "def myFunction()", "function = myFunction()"], "correct_answer": 0}
    ],
    "python": [
        {"id": 10, "text": "What is a correct syntax to output 'Hello World' in Python?", "options": ["echo('Hello World')", "print('Hello World')", "p('Hello World')", "echo 'Hello World'"], "correct_answer": 1},
        {"id": 11, "text": "How do you insert a single-line comment in Python?", "options": ["// This is a comment", "/* This is a comment */", "# This is a comment", "-- This is a comment"], "correct_answer": 2},
        {"id": 12, "text": "What is the correct file extension for Python files?", "options": [".pyt", ".py", ".pt", ".python"], "correct_answer": 1}
    ],
    "react": [
        {"id": 13, "text": "Which of the following is used in React to increase performance?", "options": ["Virtual DOM", "Original DOM", "Both A and B", "None of the above"], "correct_answer": 0},
        {"id": 14, "text": "What is a state in React?", "options": ["A permanent storage.", "Internal storage of the component.", "External storage of the component.", "None of the above."], "correct_answer": 1},
        {"id": 15, "text": "Identify the hook used to perform side effects in functional components:", "options": ["useState", "useEffect", "useContext", "useReducer"], "correct_answer": 1}
    ],
    "vue": [
        {"id": 16, "text": "Which directive is used for two-way data binding in Vue?", "options": ["v-bind", "v-model", "v-on", "v-data"], "correct_answer": 1},
        {"id": 17, "text": "How do you conditionally render an element in Vue?", "options": ["v-if", "v-show", "Both A and B", "v-condition"], "correct_answer": 2},
        {"id": 18, "text": "Which lifecycle hook is called after the instance has been mounted?", "options": ["mounted", "created", "updated", "destroyed"], "correct_answer": 0}
    ],
    "node": [
        {"id": 19, "text": "Which module is used to create a web server in Node.js?", "options": ["http", "url", "fs", "path"], "correct_answer": 0},
        {"id": 20, "text": "Node.js is built on which engine?", "options": ["SpiderMonkey", "V8", "Chakra", "JavaScriptCore"], "correct_answer": 1},
        {"id": 21, "text": "How do you install a package using npm?", "options": ["npm get <package>", "npm install <package>", "node install <package>", "npm fetch <package>"], "correct_answer": 1}
    ],
    "ts": [
        {"id": 22, "text": "What is the primary purpose of TypeScript?", "options": ["To add static types to JavaScript.", "To replace JavaScript.", "To make JavaScript run faster.", "To compile to machine code."], "correct_answer": 0},
        {"id": 23, "text": "Which extension is used for TypeScript files?", "options": [".js", ".tsx", ".ts", ".type"], "correct_answer": 2},
        {"id": 24, "text": "How do you define an interface in TypeScript?", "options": ["type InterfaceName {}", "interface InterfaceName {}", "class InterfaceName {}", "struct InterfaceName {}"], "correct_answer": 1}
    ],
    "sql": [
        {"id": 25, "text": "Which SQL statement is used to completely remove a table from a database?", "options": ["DELETE TABLE", "DROP TABLE", "REMOVE TABLE", "TRUNCATE TABLE"], "correct_answer": 1},
        {"id": 26, "text": "Which SQL clause is used to filter records?", "options": ["FILTER", "WHERE", "ORDER BY", "GROUP BY"], "correct_answer": 1},
        {"id": 27, "text": "What does SQL stand for?", "options": ["Structured Query Language", "Strong Question Language", "Structured Question Language", "System Query Language"], "correct_answer": 0}
    ],
    "mongodb": [
        {"id": 28, "text": "MongoDB is a type of which database?", "options": ["Relational", "Document", "Graph", "Key-Value"], "correct_answer": 1},
        {"id": 29, "text": "Which format does MongoDB use to store data?", "options": ["XML", "JSON", "BSON", "CSV"], "correct_answer": 2},
        {"id": 30, "text": "Which shell command is used to show all databases?", "options": ["show dbs", "list databases", "show databases", "display dbs"], "correct_answer": 0}
    ],
    "graphql": [
        {"id": 31, "text": "In GraphQL, what is used to fetch data?", "options": ["Query", "Mutation", "Subscription", "Fragment"], "correct_answer": 0},
        {"id": 32, "text": "What is used to modify data in GraphQL?", "options": ["Query", "Mutation", "Update", "Change"], "correct_answer": 1},
        {"id": 33, "text": "Which protocol is primarily used by GraphQL over the network?", "options": ["FTP", "SMTP", "HTTP", "WS"], "correct_answer": 2}
    ],
    "git": [
        {"id": 34, "text": "Which command is used to initialize a new Git repository?", "options": ["git start", "git init", "git new", "git create"], "correct_answer": 1},
        {"id": 35, "text": "How do you stage all modified files in Git?", "options": ["git add .", "git commit -a", "git push", "git stage all"], "correct_answer": 0},
        {"id": 36, "text": "What command checks the current state of the repository?", "options": ["git state", "git status", "git check", "git log"], "correct_answer": 1}
    ],
    "docker": [
        {"id": 37, "text": "What is the core component of Docker that runs background processes?", "options": ["Docker Image", "Docker Container", "Docker Daemon", "Docker Hub"], "correct_answer": 2},
        {"id": 38, "text": "Which command is used to list all running containers?", "options": ["docker list", "docker ps", "docker containers", "docker show"], "correct_answer": 1},
        {"id": 39, "text": "What file is used to build a Docker image?", "options": ["Dockerbuild", "Dockerfile", "Dockerimage", "docker-compose.yml"], "correct_answer": 1}
    ],
    "nextjs": [
        {"id": 40, "text": "What type of rendering does Next.js support by default?", "options": ["Client-Side Rendering (CSR)", "Server-Side Rendering (SSR)", "Static Site Generation (SSG)", "Both SSR and SSG"], "correct_answer": 3},
        {"id": 41, "text": "Which component is used for client-side navigation in Next.js?", "options": ["<a>", "<Nav>", "<Link>", "<Router>"], "correct_answer": 2},
        {"id": 42, "text": "Where do you define API routes in a Next.js App directory?", "options": ["pages/api", "api/", "app/api", "src/api"], "correct_answer": 0} # or route.ts in app router
    ]
}

def get_categories():
    return CATEGORIES

def get_questions_by_category(category_id: str):
    return QUESTIONS.get(category_id, [])
