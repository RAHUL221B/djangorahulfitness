<img src="https://raw.githubusercontent.com/wger-project/wger/master/wger/core/static/images/logos/logo.png" width="100" height="100" />

# wger


wger (ˈvɛɡɐ) Workout Manager is a free, open source web application that help
you manage your personal workouts, weight and diet plans and can also be used
as a simple gym management utility. It offers a REST API as well, for easy
integration with other projects and tools.

For a live system, refer to the project's site: <https://wger.de/>

![Workout plan](https://raw.githubusercontent.com/wger-project/wger/master/wger/software/static/images/workout.png)

## Installation

These are the basic steps to install and run the application locally on a Linux
system. There are more detailed instructions, other deployment options as well
as an administration guide available at <https://wger.readthedocs.io> or locally
in your code repository in the docs folder.

Please consult the commands' help for further information and available
parameters.


### Docker

Useful to just try it out. Check the READMES in wger/extras/docker on how to use
the wger/devel docker image or the docker-compose file for development:

```shell script
    docker run -ti --name wger.apache --publish 8000:80 wger/apache
```

Then just open <http://localhost:8000> and log in as **admin**, password **admin**


### Development version (from git)

**Note:** You can safely install from master, it is almost always in a usable
and stable state.


Install the necessary packages

```shell script
sudo apt-get install python3-dev nodejs npm git
sudo npm install -g yarn sass
```

Make a virtualenv where we will install the python packages

```shell script
python3 -m venv venv-wger
source venv-wger/bin/activate
```

Start the application. This will download the required JS and CSS libraries
and create a SQlite database and populate it with data on the first run. If
you want to use another database, edit the settings.py file before calling
bootstrap. You will need to create the database and user yourself.

```shell script
git clone https://github.com/wger-project/wger.git
cd wger
pip install -r requirements.txt
python setup.py develop
wger create-settings
wger bootstrap
python manage.py runserver
```

Log in as: **admin**, password **admin**

After the first run you just start django's development server::

```shell script
python manage.py runserver
```


### Command line options

You can get a list of all available commands by calling ``wger`` without any
arguments:

* `bootstrap` Performs all steps necessary to bootstrap the application
* `config-location` Returns the default location for the settings file
   and the data folder
* `create-or-reset-admin` Creates an admin user or resets the password
   for an existing one
* `create-settings` Creates a local settings file
* `load-fixtures` Loads all fixtures
* `migrate-db` Run all database migrations
* `start` Start the application using django's built in webserver

To get help on a specific command: ``wger <command> --help``.


## Contact

Feel free to contact us if you found this useful or if there was something that
didn't behave as you expected. We can't fix what we don't know about, so please
report liberally. If you're not sure if something is a bug or not, feel free to
file a bug anyway.

* **gitter:** <https://gitter.im/wger-project/wger>
* **issue tracker:** <https://github.com/wger-project/wger/issues>
* **twitter:** <https://twitter.com/wger_project>


## Sources

All the code and the content is available on github:

<https://github.com/wger-project/wger>


## License

The application is licensed under the Affero GNU General Public License 3 or
later (AGPL 3+).

The initial exercise and ingredient data is licensed additionally under one of
the Creative Commons licenses, see the individual exercises for more details.

The documentation is released under a CC-BY-SA: either version 4 of the License,
or (at your option) any later version.

Some images were taken from Wikipedia, see the SOURCES file in their respective
folders for more details.
