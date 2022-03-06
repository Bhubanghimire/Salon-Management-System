document.write(`
<!-- Navigation Bar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-black py-4 fixed-top">
    <div class="container-fluid">
        <a class="navbar-brand px-4" href="#">Lookisimo</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
            aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0 mx-auto">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Services</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Contact Us</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Review</a>
                </li>
            </ul>
            <ul class="d-flex navbar-nav gap-4">
                
                <!-- Show this for loggedin user -->
                <li class="nav-item dropdown btn btn-light">
                    <a class="nav-link dropdown-toggle text-black" href="#" id="navbarDropdown" role="button"
                        data-bs-toggle="dropdown" aria-expanded="false">
                        UserName
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item" href="#">My Profile</a></li>
                        <li><a class="dropdown-item" href="#">Settings</a></li>
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li><a class="dropdown-item" href="#">Logout</a></li>
                    </ul>
                </li>

                <!-- Show this for guest -->
                <li class="nav-item btn btn-light">
                    <a class="nav-link text-black" href="#">Sign In</a>
                </li>

                <li class="nav-item btn btn-primary">
                    <a class="nav-link text-white" href="#">Book Now</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
`);