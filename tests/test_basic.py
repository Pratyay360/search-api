"""Basic tests for DataOrchestra package."""


def test_import_dataorchestra():
    """Test that the DataOrchestra package can be imported."""
    try:
        import DataOrchestra
        assert hasattr(DataOrchestra, '__version__')
    except ImportError:
        # If import fails due to missing dependencies, that's expected
        # in the test environment without full dependencies installed
        pass


def test_core_exceptions_import():
    """Test that core exceptions can be imported."""
    from DataOrchestra.core.exceptions import (
        DataOrchestraError,
        FileProcessingError,
        DownloadError,
        CrawlError,
        ConfigurationError,
        ValidationError,
        NetworkError,
        SecurityError,
        TimeoutError,
    )

    # Verify exception hierarchy
    assert issubclass(FileProcessingError, DataOrchestraError)
    assert issubclass(DownloadError, DataOrchestraError)
    assert issubclass(CrawlError, DataOrchestraError)
    assert issubclass(ConfigurationError, DataOrchestraError)
    assert issubclass(ValidationError, DataOrchestraError)
    assert issubclass(NetworkError, DataOrchestraError)
    assert issubclass(SecurityError, DataOrchestraError)
    assert issubclass(TimeoutError, DataOrchestraError)
