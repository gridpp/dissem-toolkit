# The GridPP Dissemination Toolkit

## GridPP Talks

We use a Google form to collect information about talks given by GridPP Collaboration members.

* [The Google Form](https://docs.google.com/forms/d/1_izxIHlgbKFePlH6AcSvO5rbM9ypZ9LqU5c02Ri33-I/viewform);
* [The Google Form Results](https://docs.google.com/spreadsheets/d/1ZzetaUT3VNeYw5nXW3rQeniKZ_tRvLIhWxAn8aIChkg/).

You can download the Tab Separated Value file and use it as input to the `process-talks.py` script.

```bash
$ python process-talks.py [TSV_FILE] [OUTPUT]
```

This will generate the HTML you will need to update the http://www.gridpp.ac.uk/talks page. The output is sorted by category, date, then title.
