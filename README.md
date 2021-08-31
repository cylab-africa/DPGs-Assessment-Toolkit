# Container_Tool

This is the github page for the MOSIP Container Assessment tool

Currently contains functionality for four Kubernetes Assessment Tools: Kube-hunter, Kubebench, Kubesec, Kubeaudit

Kube-hunter is used for penetration-testing and does IP based scan of the the Kubernetes node and looks for potential vulnerabilies.
Kubebench is runs tests based on whether the Kubernetes deployment meets CIS benchmarks
Kubesec security anaylsis tool for kubernetes resources. Has a scoring systeming not is not fully explained in documentation.
Kubeaudit audits various Kubernetes Clusters for security concerns by wither looking at the manifest or config files of the cluster

The Container Assessment Tool takes a list of arguments from a json file named args.json in directory args.
The tool puts the outputs of each tool into text files in the output directory

To run the tool based on the repo:
1: Build docker image: docker build -t <imagename> .
2: Run docker image: docker run --pid=host -v `pwd`:/app/dir -v /var:/var:ro -v /etc/systemd:/etc/systemd:ro -v /srv/kubernetes:/srv/kubernetes:ro -v /etc/kubernetes:/etc/kubernetes:ro -v /usr/bin/:/usr/local/mount-from-host/bin:ro -v /etc/cni/net.d/:/etc/cni/net.d:ro -v /opt/cni/bin:/opt/cni/bin:ro --name <optionalname> --rm -it <imagename> args/args.json
