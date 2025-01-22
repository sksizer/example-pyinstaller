import sqlite3
import tempfile
from collections.abc import Sequence
from pathlib import Path

from example_pyinstaller.model import RuntimeTest, TestResult, TestStatus


def run_sqlite_test() -> Sequence[TestResult]:
    """Test SQLite database operations"""
    results = []
    db_path = None

    try:
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp_file:
            db_path = Path(tmp_file.name)

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE test_table (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """
        )
        conn.commit()
        results.append(
            TestResult(status=TestStatus.SUCCESS, message=f"Created SQLite database at {db_path}")
        )

        test_name = "PyInstaller Test"
        cursor.execute("INSERT INTO test_table (name) VALUES (?)", (test_name,))
        conn.commit()
        results.append(TestResult(status=TestStatus.SUCCESS, message="Inserted test data"))

        cursor.execute("SELECT name FROM test_table WHERE id = 1")
        row = cursor.fetchone()
        if row and row[0] == test_name:
            results.append(
                TestResult(status=TestStatus.SUCCESS, message=f"Retrieved data: {row[0]}")
            )
        else:
            results.append(
                TestResult(status=TestStatus.FAILURE, message="Data verification failed")
            )

        # Cleanup
        conn.close()
        db_path.unlink()
        results.append(TestResult(status=TestStatus.SUCCESS, message="Database cleanup successful"))

    except Exception as e:
        results.append(
            TestResult(status=TestStatus.FAILURE, message=f"SQLite operation failed: {str(e)}")
        )
        if db_path and db_path.exists():
            try:
                db_path.unlink()
            except Exception:
                results.append(
                    TestResult(
                        status=TestStatus.WARNING, message="Failed to clean up database file"
                    )
                )

    return results


TEST = RuntimeTest(
    name="SQLite Database Test",
    description="Tests basic SQLite operations in a temporary database",
    run_test=run_sqlite_test,
)
