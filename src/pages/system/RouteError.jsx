import { useRouteError } from "react-router-dom";

export default function RouteError() {
  const error = useRouteError();

  return (
    <div className="text-center mt-20 text-red-600">
      <h1 className="text-xl font-semibold mb-2">
        Something went wrong
      </h1>
      <p className="text-sm">
        {error?.message || "Unexpected error"}
      </p>
    </div>
  );
}