from pathlib import Path


# General Settings
page_title = "Digital CV | Theodore Lee IV"
page_icon = "random"
name = "Theo"
education = """
- **Florida Atlantic University (Jan 2023 - Present)**
  
  M.S. in Data Science & Analytics 


- **Florida International University (Aug 2019 - May 2021)**

  B.A. in Psychology

- **Miami Dade College (Aug 2017 - Apr 2019)**

  A.A in Psychology 

"""
description = """
Hey I'm Theodore Lee IV, but most call me "Theo". I'm currently working towards getting my masters degree in data science. 
I'm interested in leveraging different data sources to enhance mental health treatments. Smart device data can provide vaulable insights
that could lead to more personalized care and in-the-moment treatment. My goal is to figure out how to use these data sources to improve mental
health outcomes and support providers.
"""
email = '[![Medium](https://img.icons8.com/?size=30&id=12623&format=png)](leetheoiv@gmail.com)'
social_media = {'linkdin': """[![Linkdin](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://linkedin.com/in/tlee-iv)""",
                'Github': """ [![Github](https://img.icons8.com/?size=80&id=106567&format=png)](https://github.com/leetheoiv)""",
                'Medium': """ [![Medium](https://img.icons8.com/?size=80&id=wYiGNIiB4OKj&format=png)](https://medium.com/@leetheodore24)"""
                }
relevant_work_experience = ("""
**Officer @ United States Air Force (Jan 2022 - Present)**

- Leveraged expertise in missile systems to analyze readiness statuses and availability of 
intercontinental ballistic missiles (ICBM) for launch.

- Validated accuracy of target data inputs across multiple ICBM platforms,ensuring integrity 
of critical launch parameters on over several fielded ICBMs.

**Research Assistant @ The Center for Children and Families (Sep 2021 - Jan 2022)**

- Served as an objective rater, scoring teacher responses to student behavior violations using a 
validated rubric developed by the research lab. Systematically evaluated response appropriateness 
and effectiveness for incidents common among students with ADHD.

- Coordinated with teachers to plan observational data collection sessions, optimizing scheduling to 
maximize project data quality while minimizing disruptions

**Research Assistant @ The TIES Research Lab at FIU (Dec 2020 - Jan 2022)**

- Created Google Sheets to systematically record and track relevant data for a research study 
in one centralized place. Specifically, I used the sheets to track adherence rates 
and log recruitment statistics, so I could monitor overall study progress and participant involvement

- Participated in weekly team meetings related to app machine learning algorithms, app development, participant engagement, 
device troubleshooting, team collaboration, and recruitment strategies
""")
publications = """
        - Timmons, A. C., Duong, J. B., Simo Fiallo, N., **Lee, T.**, Vo, H. P. Q., Ahle, M. W., Comer, J. S.,
          Brewer, L. C., Frazier, S. L., & Chaspari, T. (2022, December). A Call to Action on Assessing 
          and Mitigating Bias in Artificial Intelligence Applications for Mental Health. Perspectives on 
          Psychological Science, 0(0).
        - Goodman, A. C., Ouellette, R. R., D’Agostino, E. M., Hansen, E., **Lee, T.**, Frazier, S.L., (2021, 
          April). Promoting Healthy Trajectories for Urban Middle School Youth Through County-
          Funded, Parks-Based After-School Programming. Journal of Community Psychology.
        - Taylor, R., Simo Fiallo, N., **Lee, T.**, Morey, G., Floyd, J., Laguerre, W., Gomez, P., Duong, J.B., 
          & Timmons, A.C. (2021, March). Precious Moments: Examining stress and childhood 
          adversity as moderators of heart rate in romantic couples. Poster presented at FIU Virtual 
          Undergraduate Research Conference.
        - Morey, G., Gomez, P., Gallego, E., **Lee, T.**, Ramirez, M., Laguerre, W., Simo Fiallo, N., Del 
          Campo, A., Duong, J.B., & Timmons, A.C. (2021, May).  Using ecological momentary 
          assessment to examine couples’ tone, communication, and aggression during everyday 
          relationship distress. Poster abstract submitted to 2021 Association for Psychological Science
          (APS) Virtual Convention.
         """

projects = {


}

# Path Settings
current_dir = Path(__file__).parent  if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles"/"main.css"
resume_file = current_dir / "assets" / "Lee-CV.pdf"
profile_pic = current_dir / "assets" / "img" /"personal photo.png"
alert_db_pic = current_dir / "assets" / "img" / "alert_db.png"
bffrs_db_pic =current_dir / "assets" / "img" / "bffrs_db.png"
vr_experiences =current_dir / "assets" / "img" / "vr_experiences.png"