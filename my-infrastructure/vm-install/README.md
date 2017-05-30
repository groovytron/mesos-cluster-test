# Mesos/Marathon stack using libvirt and Ansible

To launch the stack with 1 mesos-master (node1) and 3 mesos-slaves (node2,
node3, node4):

1. [Download the outyet demo application](https://blog.golang.org/docker)
2. Build the container by doing: 
   1. `cd ~/go//src/github.com/golang/example/outyet`
   2. `sudo docker build -t outyet .`
3. Go to the `tuto-libvirt/vm-install` directory.
4. `sudo docker save --output=outyet.tar.gz outyet` so that
   the image will be saved in this directory.
5. Start the Mesos cluster by launching `vagrant up`.

The stack takes some time to start the first time because a lot of things
need to be done (install zookeeper, mesos, marathon, chronos, ...).
Next start up are faster once the VMs images are built.

Once the VMs have booted, you can try to access to Marathon UI at the
ip address `http://192.168.33.10:8080`.

You easily test Mesos by creating an application from Marathon UI whose
command is `python -m SimpleHTTPServer $PORT0`. This launches a HTTP server
using python. You can also test the Marathon API by launching
`curl -X POST http://192.168.33.10:8080/v2/apps -d @test.json
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
-d @outyet.json -H "Content-type: application/json"`.
