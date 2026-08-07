"""
Download MNIST, Fashion‑MNIST, CIFAR‑10 dataset for P‑AFL‑Dataset
"""
import torchvision

def main():
    # MNIST
    torchvision.datasets.MNIST(root="./data/mnist", train=True, download=True)
    torchvision.datasets.MNIST(root="./data/mnist", train=False, download=True)
    # Fashion‑MNIST
    torchvision.datasets.FashionMNIST(root="./data/fmnist", train=True, download=True)
    torchvision.datasets.FashionMNIST(root="./data/fmnist", train=False, download=True)
    # CIFAR‑10
    torchvision.datasets.CIFAR10(root="./data/cifar10", train=True, download=True)
    torchvision.datasets.CIFAR10(root="./data/cifar10", train=False, download=True)
    print("All datasets download finished!")

if __name__ == "__main__":
    main()
