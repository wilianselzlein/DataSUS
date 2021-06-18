# DataSUS

<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/wilianselzlein">
    <img src="https://lh3.googleusercontent.com/proxy/2KHtrgrIM2RjxTB62kDfnLwBoNhPXqlKnJCD59uUdtYkJ_PfxNH8ZH-skqYTKVDhD5RMiHP_XcKDOUfY3m3lPrIla50CLhzaV_KAjyk2v76n" alt="Logo" width="200" height="80">
  </a>

  <h3 align="center">DataSUS</h3>

  <p align="center">
    Exploração dos dados do DataSUS
    <br />
    <a href="https://github.com/wilianselzlein/DataSUS/issues">Report Bug</a>
    ·
    <a href="https://github.com/wilianselzlein/DataSUS/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/wilianselzlein/DataSUS)

input:  `IND.csv` (file example)

result:  `CI.xls` (file example)

### Built With

* [Python](https://python.org)
* [Spark](https://spark.apache.org/)
* [PostgreSQL](https://postgresql.org/)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

```sh
python setup.py install
```
or 
```sh
python3 -m pip install --upgrade pip
```
or 
```sh
sudo python3 -m pip install -r  requirements.txt 
```
or 
```sh
pip install -r  requirements.txt
```

<!-- USAGE EXAMPLES -->
## Spark


1. Start Apache Spark

```sh
cd /opt/spark/sbin
sudo ./start-master.sh
sudo ./start-worker.sh spark://wilian-ubuntu:7077  --cores 2 --memory 8g
```

2. Stop Apache Spark

```sh
sudo ./stop-master.sh 
sudo ./stop-workers.sh
sudo ./stop-worker.sh
```

Logging to /opt/spark/logs/spark-ivo-org.apache.spark.deploy.master.Master-1-wilian-ubuntu.out

[http://127.0.0.1:8080/](http://127.0.0.1:8080/)

[![Spark Screen Shot][spark-screenshot]](https://github.com/wilianselzlein/DataSUS)

## PostgreSQL

1. Restart PostgreSQL

```sh
sudo systemctl restart postgresql
```

## Run

1. Importer to PostgreSQL

```sh
python3 main.py
```

<!-- ROADMAP -->
## Roadmap and TODO list

See the [open issues](https://github.com/wilianselzlein/DataSUS/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Ivo - [@flonopx](https://twitter.com/flonopx) - wilianselzlein@gmail.com

Project Link: [https://github.com/wilianselzlein/DataSUS](https://github.com/wilianselzlein/DataSUS)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
SUS:
* [DataSUS](https://datasus.saude.gov.br/)
* [DataSUS2](https://www2.datasus.gov.br/DATASUS/index.php)
* [FTP DataSUS](ftp://ftp.datasus.gov.br/dissemin/publicos/)

Spark:
* [Apache Docs](https://spark.apache.org/docs/latest/quick-start.html)
* [Apache GitBook](https://mallikarjuna_g.gitbooks.io/spark/)
* [Spark By Examples](https://sparkbyexamples.com/spark/)
* [Github Spark](https://github.com/apache/spark/)
* [Spark Examples](http://spark.apache.org/examples.html)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/wilianselzlein/DataSUS/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/wilianselzlein/DataSUS/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/wilianselzlein/DataSUS/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/wilianselzlein/DataSUS/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/wilianselzlein/DataSUS/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/wilianselzlein
[product-screenshot]: https://raw.githubusercontent.com/wilianselzlein/DataSUS/master/imgs/import.jpeg
[spark-screenshot]: https://raw.githubusercontent.com/wilianselzlein/DataSUS/master/imgs/spark.png
