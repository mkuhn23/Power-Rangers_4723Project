# IEM 4723 Information Systems Design and Development

## Course Project Guidelines, Fall 2026

For the course project, teams will design and build a working information system around a real-world, data-oriented problem. The system should bring together concepts surrounding database design (SQL or NoSQL), containerization, and dashboard development demonstrating end-to-end working prototypes that are self-contained and replicable independently. Teams are encouraged to be creative in choosing a problem, and to ground their design in realistic data rather than a purely hypothetical scenario. Key questions that need to be answered when choosing a problem statement include: 
1. "Who are the stakeholders?"
2. "What is the benefit of this application to the stakeholders?"
3. "How will your proposed application scale with increasing number of users"

### Potential Project Topics

For choosing your problem statement, you can think of real-world problems like the ones mentioned.
1. A ridership and route analytics system with a dashboard identifying underused routes and peak travel times. You can use the [NYC Taxi Dataset](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) or any other open source datasets for this purpose. 
2. An IoT analysis framework for real-time equipment monitoring. You can use either the [HAI dataset](https://github.com/icsdataset/hai) or other kaggle datasets like this [one](https://www.kaggle.com/datasets/nikitamanaenkov/time-series-of-industrial-boiler-operations/data) for industrial boilers.
3. An inventory management analysis dataset such as this [one](https://www.kaggle.com/datasets/harshadashirin/inventory-mangement-analysis-sql-based-project) for a small local business, tracking products, sales transactions, and reorder points, with a dashboard summarizing daily and weekly sales.

**Each team needs to have a distinct dataset that they are working with.** To avoid conflicts I have created a file on the course assignment GitHub Page (https://github.com/disys-lab/IEM4723_Fall2026_Assignments/tree/main/project_proposal/team_datasets.md). Dataset priority is granted in the order PRs are received. Teams that submit earlier will be given precedence for their requested dataset.

### Project Components 

1. **Title.** A short, descriptive title for the project, no longer than one sentence, that clearly identifies the system being built and the domain it serves.
2. **Category.** A short label describing the domain of the project, such as retail, transportation, campus operations, or healthcare.
3. **Problem Statement.** State the real-world problem being addressed and why the information system is needed, in two paragraphs.
4. **Proposed System Design.** Describe the system architecture in under a page, covering these required components.
   - Code Management and Containerization: A GitHub repository with branches, commits and forks as deemed necessary by team members. Container development and hosting on Docker hub or the Github Container Repository (GHCR).
   - Database Management and Handling: Use either a SQL, NoSQL or a combination thereof store, retrieve and edit data records for your chosen problem set. This needs to be accompanied by technical documentation such as entity-relationship diagrams, the relational database schema and other associated design choices central to your problem.
   - Visualization Component: An interactive dashboard, built using Streamlit, that visualizes the data and supports the kinds of questions a real user of the system would ask. This has to be interactive and not static.
   Teams may also propose an optional advanced component, such as an AI agent or LLM-driven feature, building on material covered later in the course for bonus points. 
5. **Data.** Describe the dataset that that your project will use. Data should be a realistic volume of records, ideally from a public or open-source dataset. Ideally Provide proper attribution for any external data source. No credit will be given if data sources are not specified.
6. **Expected System Capabilities.** State concretely what the finished system will be able to do, in a paragraph or two. A statement such as "returns the five slowest-selling items in under a second" is stronger than a vague claim such as "the system will be efficient."

### Team Composition

Teams should have 3 members leading to 9 teams overall. There can be one team that will have two members.  

### Project Deliverables and Milestones

1. **Project Proposal (Milestone 1)**: A short 3 slide proposal listing the following.
   - Team members, up to 3 students per team.
   - Project title and category. **A GitHub URL link to your repository**
   - Problem statement describing what problem needs to be addressed.
   - Description of the proposed system design, including the database, containerization, and dashboard components.
   - Data sources.
   - Expected system capabilities.
   - Scope for potential improvement.
   - Project timeline.
2. **Project Progress Check-in (Milestone 2)**: A 3 slide submission on progress so far, key accomplishments and remaining tasks as well as a clear articulation of potential blockers as well as blockers resolved successfully. 
2. **Project Presentation (Milestone 3)**: A presentation of the finished system, delivered during the project presentation lectures near the end of the semester. Each team will have 15 minutes to present their project including a demo of their application.
4. **Final Project Report (Milestone 4)**: Prepare a final report covering the system design, the database schema, the containerization approach, and the dashboard, along with the source code and supporting materials submitted through the team's GitHub repository. Include screenshots of the entity-relationship diagram, the running containers, and the dashboard, along with a short screen-recorded demo video with captions. Credit will be given for the professionalism and completeness of the report.

### Grading Criteria

The project accounts for 35% of the overall course grade, broken down as follows.

- Project Proposal: 20% of the project grade
- Presentation: 30% of the project grade
- Project Report and Final Submission: 20% of the project grade
- **Individual Team Member Contributions as indicated by Github commit history will contribute to 30% of the project grade**. Commit logs that show sustained contributions through the semester will also be considered for this grading component.

### Rubric for Grading

1. Clarity of the Problem Statement, including which real-world process or entity is being modeled and why it matters. (Refer to the "Key Questions" presented before).
2. Description of expected system capabilities, stated concretely rather than vaguely.
3. Thoroughness of the data used, including identification of appropriate sources and justification of data quality and volume.
4. Thoroughness of the relational schema, including appropriate normalization and justification of design choices.
5. Soundness of the containerized architecture, including correct use of Docker networking, volumes, and multi-container orchestration.
6. Functionality and clarity of the Streamlit dashboard, including whether it answers realistic questions a user of the system would ask.
7. Scope for improvement, including any proposed extensions such as NoSQL caching or AI agent integration.


