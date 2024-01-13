# Huex - Control your Conbee II via CLI (Alpha Version!)

### What is Huex?

Huex is a command line based tool to control the devices you have configured in your Conbee II.

This tool utilizes the [Conbee II REST API](https://dresden-elektronik.github.io/deconz-rest-doc/).

### Setup

#### Installation

Install Huex using the following command:

```
pip install huex
```

#### API Setup

When you execute a Huex command for the first time, it will fetch your Conbee II data from the [discover page](https://phoscon.de/discover).

Example:

```
huex show all
```

After this is done, Huex will prompt you to click ENTER once you've allowed authentication on your Conbee II dashboard.

Click enter once you do so and Huex should automatically create your API key and save it.

Once this is done, you can use Huex.

### Features

Huex is in alpha version, there will be many more features to come.

Here are the current features:

- Show state of all lights:

```
huex show all
```

- Turn lights on/off

```
huex control [device_id] [action]
```
