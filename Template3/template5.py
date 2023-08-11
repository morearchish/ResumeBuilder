from jinja2 import Template

# The provided HTML template with Jinja placeholders
html_template = """
<!DOCTYPE html>
<<!DOCTYPE html>
<html>
<head>
    <title>{{ user_data.name }} - {{ user_data.job_title }}</title>
    <link rel="stylesheet" href="style.css">
    <script>
        const changeTheme = type => {
            document.documentElement.style.setProperty('--primary', `var(--${type})`);
            document.documentElement.style.setProperty('--primary-light', `var(--${type}-transparent)`);
        };
    </script>
</head>
<body>
    <header class="l-header">
        <div class="c-theme">
            <button class="c-theme__button" style="color: var(--red)" onclick="changeTheme('red')">Red</button>
            <button class="c-theme__button" style="color: var(--blue)" onclick="changeTheme('blue')">Blue</button>
            <button class="c-theme__button" style="color: var(--green)" onclick="changeTheme('green')">Green</button>
            <button class="c-theme__button" style="color: var(--mono)" onclick="changeTheme('mono')">Mono</button>
        </div>
        <div class="l-header__content l-wrapper">
            <div class="grid__col grid__col--3-of-3">
                <div class="c-toggle">
                    <button class="c-toggle__item {% if user_data.theme == 'light' %}c-toggle__item--active{% endif %}" data-theme="light">
                        <i class="c-toggle__icon" data-feather="sun"></i> Light
                    </button>
                    <button class="c-toggle__item {% if user_data.theme == 'dark' %}c-toggle__item--active{% endif %}" data-theme="dark">
                        <i class="c-toggle__icon" data-feather="moon"></i> Dark
                    </button>
                </div>
                <div class="c-media">
                    <div class="c-media__content">
                        <h2 class="l-header__title">{{ user_data.name }}</h2>
                        <p class="l-header__text"><strong>{{ user_data.job_title }}&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;{{ user_data.user_location }}</strong></p>
                        <div class="c-social">
                            {% for social_link in user_data.social_links %}
                                <a class="c-social__link" href="{{ social_link.url }}">{{ social_link.title }}</a>
                            {% endfor %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <main class="l-wrapper">
        <div class="grid__col grid__col--1-of-3">
            <h4 class="u-text--primary">Contact</h4>
            <ul class="c-list">
                <li class="c-list__item">
                    <a class="c-list__link" href="#">
                        <i class="c-list__icon" data-feather="mail"></i> {{ user_data.email }}
                    </a>
                </li>
                <li class="c-list__item">
                    <a class="c-list__link" href="#">
                        <i class="c-list__icon" data-feather="phone"></i> {{ user_data.phone }}
                    </a>
                </li>
            </ul>
            <h4 class="u-text--primary">Skills</h4>
            <h5 class="u-text--secondary">Design</h5>
            <ul class="c-list">
                {% for skill, description in user_data.key_skills.items() %}
                    <li class="c-list__item">{{ skill }} - {{ description }}</li>
                {% endfor %}
            </ul>
            <h5 class="u-text--secondary">Technical</h5>
            <ul class="c-list">
                {% for category, skills in user_data.technical_skills.items() %}
                    {% for skill in skills %}
                        <li class="c-list__item">{{ category }} - {{ skill }}</li>
                    {% endfor %}
                {% endfor %}
            </ul>
            <h4 class="u-text--primary">Education</h4>
            <ul class="c-list">
                {% for education_item in user_data.education %}
                    <li class="c-list__item">
                        <strong>{{ education_item.school }}</strong><br>
                        <span>{{ education_item.qualification }}</span><br>
                    </li>
                {% endfor %}
            </ul>
        </div>
        <div class="grid__col grid__col--2-of-3">
            <h4 class="u-text--primary">Experience</h4>
            <ul class="c-list">
                {% for experience_item in user_data.work_experience %}
                    <li class="c-list__item">
                        <strong>{{ experience_item.title }}</strong>&nbsp;- {{ experience_item.position }}<br>
                        <span class="u-text--secondary">{{ experience_item.duration }}</span>
                        <p>
                            {{ experience_item.description }}
                        </p>
                    </li>
                {% endfor %}
            </ul>
        </div>
    </main>
</body>
</html>

"""

# Sample data to populate the Jinja placeholders
candidate_data_2 = {
    "page_title": "Jane Smith - Graphic Designer",
    "name": "Jane Smith",
    "job_title": "Graphic Designer",
    "email": "jane.smith@example.com",
    "phone": "9876543210",
    "personal_profile": "A brief personal profile goes here.",
    "key_skills": {
        "Web Design": "Assertively exploit wireless initiatives rather than synergistic core competencies.",
        "Interface Design": "Credibly streamline mission-critical value with multifunctional functionalities.",
        "Project Direction": "Proven ability to lead and manage a wide variety of design and development projects in team and independent situations.",
    },
    "technical_skills": {
        "Frontend": ["XHTML", "CSS", "Javascript"],
        "Backend": ["Jquery", "PHP", "CVS / Subversion"],
        "Operating Systems": ["OS X", "Windows XP/Vista", "Linux"],
    },
    "work_experience": [
        {
            "title": "Facebook",
            "position": "Senior Interface Designer",
            "duration": "2005-2007",
            "description": "Intrinsicly enable optimal core competencies through corporate relationships. Phosfluorescently implement worldwide vortals and client-focused imperatives. Conveniently initiate virtual paradigms and top-line convergence.",
        },
        {
            "title": "Apple Inc.",
            "position": "Senior Interface Designer",
            "duration": "2005-2007",
            "description": "Progressively reconceptualize multifunctional 'outside the box' thinking through inexpensive methods of empowerment. Compellingly morph extensive niche markets with mission-critical ideas. Phosfluorescently deliver bricks-and-clicks strategic theme areas rather than scalable benefits.",
        },
        # Add more work experiences as needed
    ],
}

# Create a Jinja template object
template = Template(html_template)

# Render the template with the provided data
rendered_html = template.render(**candidate_data_2)

# Save the rendered HTML to a file or use it as needed
with open("output.html", "w") as file:
    file.write(rendered_html)
