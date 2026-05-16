const Message = ({ role, text }) => {
  return (
    <div
      style={{
        marginBottom: "10px",
        padding: "10px",
        background: role === "user" ? "#2563EB" : "#1F2937",
        borderRadius: "8px"
      }}
    >
      <strong>{role.toUpperCase()}</strong>
      <p>{text}</p>
    </div>
  );
};

export default Message;