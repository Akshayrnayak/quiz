import json

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

QUESTION_TEMPLATES = [
    ("What is the primary purpose of {title}?", ["To build applications and manage specific core tasks", "For image editing", "For sending emails", "For compiling C++"], "This is the foundational use-case of the technology, designed specifically to handle its core domain efficiently."),
    ("Which command is typically used to install {title} packages or instances?", ["npm install {id} / pip install {id} / os equivalent", "apt-remove {id}", "delete-{id}", "run-destroy {id}"], "Package managers (like npm, pip) are the standard way to install modern framework dependencies."),
    ("What is a core feature or advantage of using {title}?", ["It offers robust performance and specialized tooling", "It requires absolutely no code", "It only runs on MS-DOS", "It intentionally slows down processing"], "Modern tools are adopted primarily for their performance, ecosystem, and robust tooling support."),
    ("How do you typically start a standard new project in {title}?", ["Using its official CLI tool or initialization script", "By writing raw binary", "Pressing F1 on the keyboard", "It does not support new projects"], "Most modern frameworks offer a Command Line Interface (CLI) to scaffold projects instantly."),
    ("In the context of standard development, where does {title} primarily run?", ["Where its runtime/engine is installed (Client, Server, or DB)", "Inside the GPU only", "On the moon", "It doesn't actually run"], "Technologies rely on their specific runtime environments (like Node's V8 or the Browser) to execute."),
    ("Which of the following describes the syntax or structure of {title}?", ["It relies on defined language standards or data structures", "It is purely random characters", "It uses only emojis", "It cannot be typed"], "Every language or tool has a strict syntax or API that developers must adhere to."),
    ("Who originally developed or significantly maintains {title}?", ["A large tech corporation or dedicated open-source community", "A single anonymous individual", "The state department", "Extraterrestrials"], "Major web technologies are usually backed by giant corporations (like Meta, Google) or large open-source foundations."),
    ("What file extension or data type is most commonly associated with {title}?", ["Specific extensions like .{id}, .json, etc.", ".doc", ".mp4", ".wav"], "Extensions tell the compiler, runtime, or editor how to parse the file correctly."),
    ("How is documentation handled within {title}?", ["Using inline comments and official docs", "By guessing", "Documentation is forbidden", "Watching only movies"], "Inline comments and maintaining updated official documentation is a fundamental standard."),
    ("Which programming paradigm does {title} align with?", ["Depends on the tool (OOP, Functional, Declarative, etc.)", "Random execution paradigm", "Quantum computing only", "None"], "Paradigms dictate how you structure and think about your code in that environment."),
    ("What is the most popular IDE or editor to use with {title}?", ["VS Code or JetBrains IDEs", "MS Paint", "Command Prompt", "A physical notebook"], "Modern IDEs provide intellisense and debugging capabilities specifically tailored for web development."),
    ("Can {title} be used for large Enterprise scale applications?", ["Yes, it is widely used in massive enterprise systems", "No, it is strictly a toy tool", "Only for blogs", "Only if it is written in assembly"], "These technologies were built to scale and are actively used by Fortune 500 companies."),
    ("What does the 'Latest Version' of {title} usually bring?", ["Bug fixes, security patches, and performance improvements", "More bugs intentionally", "Removal of all features", "A completely different name"], "Semantic versioning ensures that updates bring security patches and feature optimizations."),
    ("How handles errors in {title}?", ["Using specific error handling blocks (Try/Catch) or query validations", "By ignoring them completely", "Restarting the computer automatically", "Errors do not exist"], "Proper error handling prevents applications from crashing and provides user-friendly feedback."),
    ("Which operating systems natively support or can run {title}?", ["Cross-platform (Windows, macOS, Linux)", "Only Windows 95", "Only DOS", "None"], "Modern web development tools are almost always cross-platform."),
    ("Is {title} considered open-source?", ["Generally yes, or has a massive open-source ecosystem", "No, it costs $100,000", "It is illegal to use", "No one knows"], "The explosion of web development is heavily reliant on open-source licensing."),
    ("Where do developers go for help regarding {title}?", ["Official Docs, GitHub, and StackOverflow", "The yellow pages", "Wikipedia exclusively", "It is a secret"], "The community on GitHub and StackOverflow forms the backbone of developer support."),
    ("What is the learning curve generally considered for {title}?", ["Moderate; requires understanding of its specific concepts", "Impossible to learn", "Can be mastered in 5 minutes", "Requires a PhD degree"], "Every powerful tool has domain-specific concepts (like React's state, or Docker's containers) that take time to master."),
    ("How robust is the community ecosystem for {title}?", ["Very strong with thousands of third-party libraries", "Non-existent", "Only through paid Microsoft support", "Only in Latin texts"], "A massive ecosystem of NPM/PIP packages makes building apps much faster."),
    ("What is a major anti-pattern in {title}?", ["Ignoring official best practices and state management rules", "Writing clean, documented code", "Using version control", "Testing the software"], "Anti-patterns (like directly mutating state in React) lead to massive bugs and performance issues."),
    ("Which protocol is most likely to be used alongside {title} for web APIs?", ["HTTP/HTTPS", "FTP", "SMTP", "Telnet"], "HTTP/S is the foundation of data communication for the World Wide Web."),
    ("How is data typically formatted when interacting with {title} REST APIs?", ["JSON or XML", "CSV only", "Binary executables", "Raw unformatted text"], "JSON (JavaScript Object Notation) is the universal standard for API data exchange."),
    ("How is dependency management handled in {title}?", ["Using dedicated package managers", "Manually downloading zip files every time", "Copy-pasting code from friends", "Dependencies are banned"], "Package managers (npm, pip, yarn) resolve the complex dependency tree automatically."),
    ("How do you typically debug {title} applications?", ["Using built-in debuggers, devtools, or console logs", "Guessing randomly", "Writing the code again from scratch", "Never debugging"], "Browser DevTools and IDE debuggers are critical for inspecting variables and call stacks."),
    ("What are the primary data structures utilized in {title} logic?", ["Arrays, Objects/Dictionaries, Lists", "Linked Lists exclusively", "Trees exclusively", "Just raw bytes"], "Standard high-level data structures are used to organize arrays of data and objects efficiently."),
    ("Does {title} support asynchronous operations effectively?", ["Yes, via Promises, Async/Await, or background tasks", "No, it is strictly single-threaded blocking", "Only on Thursdays", "No, it breaks the hardware"], "Asynchronous operations prevent the main thread (or UI) from freezing during network requests."),
    ("What is the typical deployment strategy for {title}?", ["Cloud hosting (AWS/Vercel), Docker containers, or CI/CD pipelines", "Mailing physical hard drives", "Cannot be deployed ever", "Running strictly locally"], "CI/CD pipelines automate testing and deployment to cloud servers like AWS or Vercel."),
    ("What is a common security consideration when using {title}?", ["Preventing injections (SQL/XSS) and validating all inputs", "Using easy root passwords", "Making all database credentials public", "Security is handled magically by the OS"], "Never trust user input; XSS and SQL Injection are the most common web vulnerabilities."),
    ("How do {title} projects usually scale under load?", ["Vertically (better hardware) and Horizontally (more instances)", "Diagonally", "They don't scale", "By buying a bigger physical monitor"], "Horizontal scaling (adding more servers/containers) is the standard for handling massive web traffic."),
    ("What is the ultimate goal of adopting {title} in a modern stack?", ["To maximize efficiency, performance, and developer experience", "To purposely slow down project delivery", "To add completely unnecessary complexity", "Just to use a modern buzzword"], "We choose specific technologies to solve specific problems efficiently and effectively.")
]

def generate_db():
    output_lines = [
        "CATEGORIES = " + json.dumps(CATEGORIES, indent=4) + "\n",
        "QUESTIONS = {\n"
    ]
    
    question_id_counter = 1
    
    for idx, cat in enumerate(CATEGORIES):
        cid = cat['id']
        ctitle = cat['title']
        
        output_lines.append(f'    "{cid}": [')
        
        for i in range(30):
            template = QUESTION_TEMPLATES[i % len(QUESTION_TEMPLATES)]
            text = template[0].format(title=ctitle, id=cid)
            options = [opt.format(title=ctitle, id=cid) for opt in template[1]]
            explanation = template[2]
            
            correct_ans_idx = i % 4
            
            final_options = [""] * 4
            for j in range(4):
                final_options[(j + correct_ans_idx) % 4] = options[j]
                
            q_obj = {
                "id": question_id_counter,
                "text": text,
                "options": final_options,
                "correct_answer": correct_ans_idx,
                "explanation": explanation
            }
            output_lines.append(f"        {json.dumps(q_obj)}" + ("," if i < 29 else ""))
            question_id_counter += 1
            
        output_lines.append("    ]" + ("," if idx < len(CATEGORIES)-1 else ""))
        output_lines.append("\n")
        
    output_lines.append("}\n")
    output_lines.append("def get_categories():\n    return CATEGORIES\n\n")
    output_lines.append("def get_questions_by_category(category_id: str):\n    return QUESTIONS.get(category_id, [])\n")

    with open("quiz_data.py", "w", encoding="utf-8") as f:
        f.writelines(output_lines)

if __name__ == "__main__":
    generate_db()
    print("Database expanded with explanations.")
