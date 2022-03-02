# tap-trello

`tap-trello` is a Singer tap for trello.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Currently the best way to use this tap is to pip install from the github repository.

You can also add this tap as a [custom plugin](https://docs.meltano.com/concepts/plugins#custom-plugins) to your Meltano project.

## Configuration

### Accepted Config Options

Tap settings:

- `developer_api_key` - Your Trello developer api key
- `access_token` - Your Trello access token

Optional:

- `start_date` - The date to sync Actions and Cards from. Format: `2010-01-01T00:00:00Z`

You can find out how to get these settings in the next section: Source Authentication and Authorization.

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-trello --about
```

### Source Authentication and Authorization

To get the settings required to use this tap go to the [Trello app-key page](https://trello.com/app-key).

#### Getting your `developer_api_key`

If you are logged in you will see a screen with the title Developer API Keys. The key shown in the grey box directly below that is your `developer_api_key`.

#### Getting your `access_token`

To get your `access_token` you need to click the `Token` at the end of the first paragraph of text on that page. This will open a new window showing what permissions you are allowing the token to have, and once you click Allow, you will be redirected to a page with a grey box with your `access_token` in.

## Usage

You can easily run `tap-trello` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-trello --version
tap-trello --help
tap-trello --config CONFIG --discover > ./catalog.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_trello/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-trello` CLI interface directly using `poetry run`:

```bash
poetry run tap-trello --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-trello
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-trello --version
# OR run a test `elt` pipeline:
meltano elt tap-trello target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
