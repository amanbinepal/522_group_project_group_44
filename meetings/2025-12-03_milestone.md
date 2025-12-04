# Meeting Minutes - 2025-12-03

**Milestone 3**  

Attendance: Aman, Emily, Ian, Vy

## Milestone 3 Discussion

- work from container?
- switch up roles?

## Fixes from Milestone 1

- [ ] Your analysis was interesting and well documented. Remember to only do EDA on training data to avoid data leakage.

  - AMAN - done

- [ ] One small note about reproducibility: Conda-lock doesn’t keep pip-installed packages, so your conda environment (from the Conda-lock file) was missing ucimlrepo and vegafusion. To avoid this, you can try installing these packages through conda directly  

  - AMAN - done

- [ ] Finally, please rename your repository to be more descriptive (e.g. something like ‘iris-classifier’). This makes it easier for other users to find you work and potentially cite it!  

  - AMAN - done

- [ ] Readme update based on comments
- [ ] Environment file pinning - Aman
- [ ] Abstract
- [ ] Intro
- [ ] Figure legend + description
- [ ] references

1) make sure to add package versions for all packagees in the environment.yml file; - Aman

2) for the docker-compose.yml and Dockfile base image, make sure to add specific version tags (otherwise it will default to latest) to ensure reproducible builds. - Aman

## Tasks

- set up folder structure - scripts, report, results, maybe add in .ipynb somehwere else - Vy
- convert to .qmd before any edits to .ipynb? - Emily
    - Quarto package install - Aman

### 1.1 Abstract code into .py

- Make sure we know what outputs are from previous .py  

- Download and save - Vy
- data split, categorize features, data validation? - Vy
- EDA - Emily
- Model Evaluation - Ian
- Chosen Model fit - Ian
- Model Predict - Ian

### 1.2 Abstract text and outputs into .qmd

- Update environment/lock/docker with Quarto - Aman

### 1.3 Update README Documentation

- Will see later as we work, who has time

### 1.4 Release

## To Do's
