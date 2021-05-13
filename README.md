# KopuruVespaCompetitionIE
IE Business School team (WaspBusters) for the [**2021 Kopuru Vespa Velutina**](https://kopuru.com/desafio/vespa-velutina/) data science competition.

This is the script+data workflow followed for each submission:
![WaspBusters workflow](https://github.com/IEwaspbusters/KopuruVespaCompetitionIE/raw/main/Competition_subs/Beeswax.jpg "THE BEESWAX is the glue that keeps it all together")

This is the Git workflow used by the team:

First, set up the Jupyter Lab environment with the [Git extension](https://github.com/jupyterlab/jupyterlab-git). This is for Windows only:
1. Install Anaconda
2. Run `conda install -c conda-forge jupyterlab-git` in the conda terminal
3. In conda terminal, run `conda install -c conda-forge nodejs`
4. In conda terminal, run `conda install -c anaconda git` (if first time installing Git, then maybe also set up your credentials: `git config --global user.name "Your name here"`
`git config --global user.email "your_email@example.com"`)
5. Open jupyterlab
6. Enable extensions (puzzle icon in the left bar)
7. Scroll down to @jupyterlab/git and click `install`
8. When jupyterlab asks to build the git extension, click `build`. Then wait for it to finish and then reload jupyterlab
9. Maybe, just maybe, a git update from the jupyterlab console may be in order `pip install --upgrade jupyterlab-git`
10. Maybe, just maybe, if the cloning doesn't work right off the bat try in the jupyterlab console `git clone <repo url>` directly
11. Still doesn't work? Reboot everything. Your laptop, Jupyter, Conda. All of it. Maybe a couple of times.
12. **DO NOT** update Anaconda navigator nor Jupyter Lab beyond what comes by default in the initial install.

Now, let's get to work:
1. One-time only: **"CLONE"** this repository in your local JupyterLab environment, using the [HTTPS URL](https://github.com/IEwaspbusters/KopuruVespaCompetitionIE.git)
4. **PULL**. For each_time_you_edit in range([now, deadline, daily]), before editing, make sure you always **"Pull from remote"** the latest version of the repo
5. Edit whatever script and data you need in the corresponding submission and batch folder. **.IPYNB** files are preferred in most cases
6. **STAGE** any _Changed_ or _Untracked_ files (by clicking on the "+") that you want to commit (i.e. "save")
7. **COMMIT**. Write a short Summary of the changes you are introducing and then click **Commit**
8. **PUSH**. Now **Push to remote** the commit you just made to see them reflected in [the WaspBuster's GitHub repo](https://github.com/IEwaspbusters/KopuruVespaCompetitionIE)
