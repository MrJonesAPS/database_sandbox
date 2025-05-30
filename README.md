A sandbox for my class Advanced Database Management (https://ict.gctaa.net/sections/itd256/)
at [Arlington Tech](https://arlingtontech.apsva.us/) 
where we explore several different
database technologies: Sqlite, PostgreSQL (and pgAdmin), Redis, MongoDB, CockroachDB, Neo4j

Inspired by https://github.com/pamelafox/postgresql-playground/tree/main - thanks @pamelafox for the idea!

To use this repo:
- If you want to be able to save your work, start by forking this repo
- click on the green "<>Code" button at the top of the page, select the "Codespaces" tab, and then "Create codespace on main."
- This will open a github codespace (basically VSCode inside your browser) and will take a few minutes to spin up all of the databases
- Run db_test.py to confirm that all of the databases are running and you're able to connect to them
- Comment out the database connections you don't need, and then start working!

You can also run this on local VSCode with the [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
To run with this extension (or if you modify any of the config files in your codespace, make sure to run the command "Dev Containers: Rebuild and Reopen in Container")

The Docker images for Neo4j, CockroachDB, and PostgreSQL also include web UIs, which you can launch from the "Ports" tab.
(I haven't gotten the Neo4j web UI to work from Github Codespaces, but it works in VSCode locally). 

Note: I'm launching all databases automatically every time, even though we never actually use all of these together. My goal in creating this was to have something
very easy for my database students to use, but startup can be slow. For any individual project, you should fork this and make a modified version that comments out whichever databases you aren't using.
