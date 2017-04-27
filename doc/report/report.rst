.. MIP App Framework documentation master file, created by
   sphinx-quickstart on Tue Feb  7 00:24:36 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MIP App Framework's documentation!
=============================================

.. .. toctree::
   :maxdepth: 2
   :caption: Contents:


Introduction
============

Ce document décrit la réalisation d'une infrastructure de type SaaS (Software
as a Service) dans le cadre d'un travail de bachelor.

Outils et technologies utilisées
--------------------------------

Cette partie décrit les différentes technologies et outils utilisés pour la
réalisation du projet. Elle mélange de nombreux outils permettant de gérer
des machines virtuelles, gérer des containers ou encore de mettre en
communication plusieurs containers. L'ensemble des logiciels présentés sont
open-source.

Vagrant
~~~~~~~

Vagrant est un outil open source permettant de créer et gérer des machines
virtuelles. Il fonctionne avec un fichier `Vagrantfile` décrivrant
les propriétés de la machine virtuelle telles que la distribution utilisée
son nom et sa configuration réseau par exemple. Notez que ce fichier est
écrit en Ruby.

On peut créer un `Vagrantfile` facilement grâce à la commande
:code:`vagrant init bento/centos-7.1` qui crée un `Vagrantfile` basé sur une machine
CentOS par exemple. On peut ensuite lancer la machine virtuelle en se plaçant
dans le dossier contenant le `Vagrantfile` et en utilisant la commande
:code:`vagrant up`. On peut ensuite se connecter à la machine virtuelle en ssh
grâce à la commande :code:`vagrant ssh`. On peut éteindre la machine virtuelle
démarrée avec la commande `vagrant halt` ou `vagrant destroy` si on désire
effacer complètement la machine virtuelle.

Vagrant a besoin d'une solution de virtualisation pour fonctionner. Il supporte
**Virtualbox**, **Docker** et également **KVM** qui remplissent ce rôle.
Il est généralement utilisé avec Virtualbox mais il semble que KVM soit plus
performant.


Mesos
~~~~~

Développé à l'université de Berkley, **Mesos** permet de gérer des clusters de
machines.
Ce logiciel propose plusieurs outils permettant l'isolation de CPU, de
mémoire et de fichiers. Utiliser un tel logiciel permet donc de partager
les ressources d'une infrastructure. En général, Mesos est utilisé
conjointement avec **Marathon**. Mesos est utilisé par de grandes entreprises
telles que Twitter, Airbnb, Apple ou encore Verizon.

Marathon
~~~~~~~~

**Marathon** est un outils de PaaS (Platform as a service). Il permet de
l'orchestration de containers et faire du scaling (gestion des ressources
et démarrage/arrêt de machines) pour différents services contenus dans
des containers. Marathon propose une *API REST* implémentée en *Scala*.

ZooKeeper
~~~~~~~~~

*ZooKeeper* permet de syncronizer différents services entre eux grâce à
un système de stockage clé-valeur implémenté
sous forme d'un système de fichiers. Les clients peuvent lire ou écrire
dans ce système de fichier pour se transmettre des informations et ainsi
partager leurs configurations (accès aux serveurs de base de données, accès
aux serveurs HTTP, etc.). ZooKeeper est utilisé par des entreprises comme
Yahoo! et Reddit.

Avant de démarrer, le serveur ZooKeeper doit être initialisé avec un ID.
Pour par exemple l'initialiser avec un l'ID *1*, il suffit de lancer la
commande `sudo -u zookeeper zookeeper-server-initialize --myid=1`.
Une fois initialisé, le serveur peut être démarré. Comme il se comporte
comme un service sur UNIX, il suffit de lancer la commande
`sudo service zookeeper-server start`. On peut l'appeler avec `enable`
si l'on veut que le serveur démarre au boot de la machine et ainsi éviter
de devoir le démarrer manuellement. On peut le stopper avec `start`.

On peut interagir avec ZooKeeper au-travers de son client à l'aide de
la commande `zookeeper-client`.

Tests
=====

Ceci est un test pour insérer du code dans le document.

.. code:: python

    print("Hello World!")

Quelques tests: test1, test2, etc.

.. code-block:: php

    <?php
        $customers = Customer::all();
        echo "toto";
    ?>


Fin des tests.


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
