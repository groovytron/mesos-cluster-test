# mesos-cluster-test

This repo contains files allowing to setup
a [Mesos Marathon](https://mesosphere.github.io/marathon/) cluster using
[Vagrant](https://www.vagrantup.com/) and [Ansible](http://docs.ansible.com/ansible/playbooks.html).
The main goals of this repo were to help me to understand how Vagrant and
Ansible work together and teach me how the Mesos Marathon can be setup
and for what purpose.

You will need to have the following softwares installed on your system:

* Vagrant
* Ansible
* A VM hypervisor like [libvirt/KVM](https://libvirt.org/),
  [Docker](https://www.docker.com/) or
  [Virtualbox](https://www.virtualbox.org/wiki/VirtualBox)

Using libvirt/KVM is strongly recommended as it is known to be lighter
(less resource consuming) than the other supervisors.

The box used to build the machines is [centos/7](https://atlas.hashicorp.com/centos/boxes/7/versions/1704.01)
which contains a CentOS operating system.

# Usage

To launch the stack with 1 mesos-master (node1) and 3 mesos-slaves (node2,
node3, node4):

1. [Download the outyet demo application](https://blog.golang.org/docker)
2. Build the container by doing: 
   1. `cd ~/go//src/github.com/golang/example/outyet`
   2. `sudo docker build -t outyet .`
3. Go to the project's `my-cluster/vm-install` directory.
4. `sudo docker save --output=outyet.tar.gz outyet` so that
   the image will be saved in this directory.
5. Start the Mesos cluster by launching `vagrant up` in the
  `vm-install` directory.

The stack takes a few minutes to start the first time because a lot of things
need to be done (install zookeeper, mesos, marathon, chronos, ...).
Next start up are faster once the VMs images are built.

Once the VMs have booted, you can try to access to Marathon UI at the
ip address `http://192.168.33.10:8080`.

You can easily test Mesos Marathon by creating an application
from Marathon UI whose command is `python -m SimpleHTTPServer $PORT0`.
This launches a HTTP server using python. You can also test the Marathon API by launching
`curl -X POST http://192.168.33.10:8080/v2/apps -d @/vagrant/test.json
-H "Content-type: application/json"`. You should then see the application
running. You can then scale up the application to see if mesos-dns works
and every instance gets its own access port and subdomain.

You can test if mesos-dns works by launching
`curl http://192.168.33.10:8123/v1/hosts/test.marathon.mesos`.

If you want to check docker containers deployment works, you can try to
deploy the outyet application through Marathon UI by creating
an application whose command is `sudo docker run --publish $PORT0:8080
--name test --rm outyet`.
Alternatively, you can use Marathon API and push the app with `curl`
by launching `curl -X POST http://192.168.33.10:8080/v2/apps
-d @/vagrant/outyet.json -H "Content-type: application/json"`.

